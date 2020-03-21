import io, os
import datetime, time
from PIL import Image
import picamera
import ffmpy


def create_file_location(folder):
    count = 0
    while True:
        loc = folder + '/' + str(count)
        if (os.path.exists(loc)):
            count += 1
        else:
            os.makedirs(loc)
            return str(count)
    #filename = datetime.datetime.strftime(ftime, '%y%m%d-%H%M%S')
    #filename = 'motion' + timestring
    #return filename

def create_folder_name(time):
    date = datetime.datetime.strftime(time, '%Y-%m-%d')
    return date
 
def make_folder(path, foldername):
    #count = 0
    combine = path + '/' + foldername
    if(os.path.exists(combine)):
        return True, combine
    elif not os.path.exists(combine):
        os.makedirs(combine)
        return True, combine
    return False #i think this isnt reachable but jic

def create_base_image(camera):
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg', use_video_port=True)
    stream.seek(0)
    return Image.open(stream)

def crate_final_loc_string(path, fnum):
    ret = path + '/' + fnum + '/'
    return ret

def combine_recordings(path, num):
    before = path + '/' + 'before.h264'
    after = path + '/' + 'after.h264'
    #tired and dont feel like coming up with a good name
    afsdjlk = 'concat:{0}|{1}'.format(before, after)
    combined = path + str(num) + '.h264'
    '''ff = FFmpeg(
        inputs={before : None, after : None},
        outputs={combined : '-c copy'}
    )'''
    os.system("ffmpeg -i \"{0}\" -c copy {1}".format(afsdjlk, combined))
    os.system('rm {0} {1}'.format(before, after))