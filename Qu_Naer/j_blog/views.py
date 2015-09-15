from django.shortcuts import render
from utils.json_functions import http_json_wraper
from j_blog.logic import BlogLogic

# Create your views here.
@http_json_wraper
def get_all_topic_v(request):
    """
    """
    return BlogLogic.get_all_topic_l()

@http_json_wraper
def get_time_index_v(request):
    """
    """
    return BlogLogic.get_time_index_l()

def get_post_by_time_index_v(request):
    """
    """
    if request.method != "GET":
        return dict(msg="Unexpected request method in function j_blog::views::get_post_by_time_index_v()",
                    warn="OK")
    else:
        try:
            if 'time_index' in request.GET:
                pass
        except Exception as e:
            return dict(msg="Error msg from function j_blog::views::get_post_by_time_index_v(), %s" % str(e))

def get_post_by_topic_v(request):
    """
    """
    if request.method != "GET":
        return dict(msg="Unexpected request method in function j_blog::views::get_post_by_time_index_v()",
                    warn="OK")
    else:
        pass

def test(request):
    """
    """
    return render(request, 'j_blog/index_list.html',{'index_type': 'time_index',
                                                     'index_content': '2015-03',
                                                     'content': [{'title': 'Hello world!',
                                                                'author': 'Jianbin, Hong'}]})
