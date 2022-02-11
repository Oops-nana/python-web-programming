from django import forms

# 폼을 정의하기 위해서는 django.forms모듈의 Form클래스를 상속받아 클래스를 정의하면 된다.


class PostSearchForm(forms.Form):
    # charfield는 textinput위젯으로 표현됨. label인자는 폼의 레이블이 되고
    # search_word는 Input태그에 대한 name속성이 되어 사용자기 입력한 값을 저장하는 데 사용됨 -> <input type="text">를 만든 것과 동일
    search_word = forms.CharField(label='Search Word')
