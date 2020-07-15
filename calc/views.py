from django.shortcuts import render

expression = []

def calculate(request):
    result = ''
    if request.GET:
        if request.GET.get('number'):
            expression.append(request.GET['number'])

        if request.GET.get('operation'):
            expression.append(request.GET['operation'])
        
        if request.GET.get('calculate'):
            exp_str = ''.join(expression)
            result = eval(exp_str)
            print(result)

    return render(request, 'calc/index.html', context={ 
        'result': result,
        'expression': ''.join(expression)
        })