from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False


class Is_get_or_patch(BasePermission):
    def has_permission(self,request,view):
        allowed_methods=['GET','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False



class sunny_permission(BasePermission):
    def has_permission(self,request,view):
        username=request.user.username  # user is an model object
        # we get empty string (  ''   which is of length zero and is even )  as a result of  request.user.username if User is NOT Authenticated
        if username.lower()=='sunny':
            return True
        elif (len(username) %2==0) and (username.lower()!='sunny') and (request.method in SAFE_METHODS):
            return True
        else:
            return False
