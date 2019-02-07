from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
# Better to create a child class of   PageNumberPagination class with custom our own custom properties for enabling pagenation Locally
class MyPagination(PageNumberPagination):
    page_size=5
    # http://127.0.0.1:8000/list-api/?page=7    will give us records on page 7 ... ie.. from 31 to 35
    # (?page) is the default query param   we can set it to (?mypage) by using     page_query_param
    page_query_param='mypage'

    # http://127.0.0.1:8000/list-api/?mypage=7&page_size=13   will only work when we set     page_size_query_param
    page_size_query_param='page_size'  # we can set it to anything eg page_size_query_param='num'

    max_page_size=15  #  http://127.0.0.1:8000/list-api/?page_size=20     will give 15 record instead of 20

    #  http://127.0.0.1:8000/list-api/?mypage=last will give last page containing 5 records
    last_page_strings=('endpage',)
    #  http://127.0.0.1:8000/list-api/?mypage=endpage will give last page containing 5 records

class MyPagination2(LimitOffsetPagination):
    #pass # http://127.0.0.1:8000/list-api/    will give 10 records from beginning
         # default limit is PAGE_SIZE declared globallly in settings .py
         # defalut offset is the first record available in database

    # http://127.0.0.1:8000/list-api/?limit=13&offset=20
    default_limit=15   # http://127.0.0.1:8000/list-api/?offset=20     will give 21 to 35
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=20
    # http://127.0.0.1:8000/list-api/?mylimit=25&myoffset=40     will givr 41 to 60



class MyPagination3(CursorPagination):
    pass
    # we get error ....   Cannot resolve keyword 'created' into field. Choices are: eaddr, ename, eno, esal, id
    # by defalut it is expecting 'created' field
    # ordering='-created'  is the defaulyt value
    # so we require to specify our own ordering for solving this error
    # ordering='esal'   for ascending
    page_size=5
    ordering='-esal'
