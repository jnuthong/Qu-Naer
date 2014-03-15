
def print_object(obj):
    print (', '.join(['%s:%s' % item for item in obj.__dict__.items()]))