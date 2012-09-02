import re
import urllib
from xml.dom import minidom


def getPhoto(apiKey, nsid, photoNumber, popular):

    popular = popular.lower()

    if popular == 'p':
        popular = 'interestingness-desc'
    else:
        popular = 'date-posted-desc'

    photoSearchUrl = "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={0}&user_id={1}&per_page=1&page={2}&sort={3}".format(apiKey, nsid, photoNumber, popular)
    dom = minidom.parse(urllib.urlopen(photoSearchUrl))

    photoNode = dom.getElementsByTagName("photo")[0]
    photo = FlickrPhoto()
    photo.id = photoNode.getAttribute("id")
    photo.server = photoNode.getAttribute("server")
    photo.farm = photoNode.getAttribute("farm")
    photo.secret = photoNode.getAttribute("secret")
    return photo





def getNSID(apiKey, username):

    if not 'http://' in username:
        username = 'http://www.flickr.com/photos/' + username

    if not re.match("([0-9]+@N[0-9]+)", username):
        lookupUrl = "http://api.flickr.com/services/rest/?method=flickr.urls.lookupUser&api_key={0}&url={1}".format(apiKey, username)
        dom = minidom.parse(urllib.urlopen(lookupUrl))
        userNode = dom.getElementsByTagName("user")[0]
        nsid = userNode.getAttribute("id")
    else:
        nsid = username

    return nsid



def getPhotoPageUrl(selectedPhoto, nsid):
    return "http://www.flickr.com/photos/{0}/{1}".format(nsid, selectedPhoto.id)




def getImageUrl(selectedPhoto, size):

    size = size.lower()
    sizePrefix = '_'

    if size == 'm' or size == 'small':
        size = 'm'
    elif size == 's' or size == 'square':
        size = 's'
    elif size == 't' or size == 'thumb' or size == 'thumbnail' or size == 'tiny':
        size = 't'
    elif size == 'z' or size == 'medium640' or size == 'medium 640':
        size = 'z'
    elif size == 'b' or size == 'large' or size == 'big':
        size = 'b'
    elif size == '' or size == 'medium' or size == 'med' or size == 'x':
        sizePrefix =  ''
        size = ''

    size = sizePrefix + size

    return "http://farm{0}.static.flickr.com/{1}/{2}_{3}{4}.jpg".format(selectedPhoto.farm, selectedPhoto.server, selectedPhoto.id, selectedPhoto.secret, size)


def getPhotoIdFromUrl(flickrUrl):

    if flickrUrl:
        r = re.compile("/photos/[^/]+/(?P<photoid>[0-9]+)")
        if r.search(flickrUrl):
            return r.search(flickrUrl).group("photoid")


    return None



def getPhotoInfo(apiKey, photoId):


    photoInfoUrl = "http://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key={0}&photo_id={1}"\
                        .format(apiKey, photoId)
    dom = minidom.parse(urllib.urlopen(photoInfoUrl))

    photoNode = dom.getElementsByTagName("photo")[0]
    photo = FlickrPhoto()
    photo.id = photoNode.getAttribute("id")
    photo.server = photoNode.getAttribute("server")
    photo.farm = photoNode.getAttribute("farm")
    photo.secret = photoNode.getAttribute("secret")
    return photo


def getLargestSizeUrl(apiKey, photoId):
    """
    Gets the largest available photo size for a photo, but not the original
    """
    largestUrl = None
    photoSizesUrl = "http://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={0}&photo_id={1}"\
                    .format(apiKey, photoId)

    dom = minidom.parse(urllib.urlopen(photoSizesUrl))

    sizeNodes = dom.getElementsByTagName("size")

    largestWidth = 0

    for sizeNode in sizeNodes:
        if largestWidth <= 1024 or not sizeNode.getAttribute("label") == "Original":
            largestUrl = sizeNode.getAttribute("source")
            largestWidth = int(sizeNode.getAttribute("width"))

    return largestUrl



class FlickrPhoto:
    id = ''
    server = ''
    farm = ''
    secret = ''
