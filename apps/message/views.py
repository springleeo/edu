from django.shortcuts import render

from .models import UserMessage


def get_form(request):
    # 查询数据库数据
    # all_message = UserMessage.objects.all()

    # all_message = UserMessage.objects.filter(name='和平')
    # for message in all_message:
    #     print(message.name)
    #     print()

    # 保存数据到数据库
    # message = UserMessage()
    # message.name = '夏天'
    # message.email = '1@4.com'
    # message.address = '福州'
    # message.save()

    # 表单添加数据
    # if request.method == 'POST':
    #     message = UserMessage()
    #     message.name = request.POST.get('name', '')
    #     message.email = request.POST.get('email', '')
    #     message.address = request.POST.get('address', '')
    #     message.message = request.POST.get('message', '')
    #     message.save()

    # 表单删除数据
    # if request.method == 'POST':
    #     message = UserMessage.objects.filter(name=request.POST.get('name'))
    #     message.delete()

    # 数据库数据返回前端
    all_message = UserMessage.objects.filter(name='和平')
    if all_message:
        message = all_message[0]

    if request.method == 'POST':
        if message.name == request.POST.get('name'):
            message.email = request.POST.get('email')
            message.address = request.POST.get('address')
            message.message = request.POST.get('message')
            message.save()

    print()

    return render(request, 'message_form.html', {'my_message': message})
