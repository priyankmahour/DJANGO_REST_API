from rest_framework.pagination import PageNumberPagination
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
