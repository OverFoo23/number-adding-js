"""from browser import document,html
container = document['container']
todo_list = html.H1("Computer Guess Number")
container <= todo_list

list_div= html.DIV(id='list')
container <= list_div


def add_item(event):
    if event.key == 'Enter':
        list_div <= html.LI(html.INPUT(type='checkbox') + ' ' + input.value  )
        input.value = ''  


input = html.INPUT(type='text',id='input').bind('keydown',add_item)
container <= input


def clear_list(event):
    list_div.html = ''




container <= html.BUTTON('Clear List').bind('click', clear_list)"""





    #items = ['hırhır','hır','hırrım sopası']
    #for item in items:
    #container <= html.LI(item)













