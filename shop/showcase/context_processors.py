

def admin_user(request):
    return {'admin_user': request.user.groups.filter(name='admin').exists()}