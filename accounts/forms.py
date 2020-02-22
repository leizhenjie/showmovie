# -*- coding: utf-8 -*-
# @Author:LZJ
# @Time: 
# @Description:
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from accounts.models import User
from django.contrib.auth.hashers import check_password as auth_check_password


class LoginForm(forms.ModelForm):
    captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={"id": "code", "maxlength": "6", "autocomplete": "off", "class": "layui-input", "placeholder": "请输入验证码"}))

    class Meta:
        model = User
        fields = ['username', 'password']
        # exclude = ()

        widgets = {
            'username': widgets.TextInput(
                attrs={"id": "account", "lay-verify": "required", "class": "layui-input",
                       "placeholder": "请输入用户名", "maxlength": "20", "autocomplete": "off", "autofocus": "autofocus",
                       "name": "username"}),
            'password': widgets.PasswordInput(
                attrs={"id": "password", "lay-verify": "required", "class": "layui-input",
                       "placeholder": "请输入密码", "maxlength": "20", "autocomplete": "off", "name": "password"}),
        }
        #

    def check_password(self):
        print('check password')
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
            return user, auth_check_password(password, user.password)
        except:
            return None, False


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=16,
                               widget=widgets.TextInput(
                                   attrs={"class": "layui-input", "id": "username", "placeholder": "请输入用户名",
                                          "maxlength": "16", "lay-verify": "required|usr", "autofocus": "autofocus",
                                          "autocomplete": "off", "name": "username"}))
    mobile = forms.CharField(label="手机号", max_length=11, widget=widgets.TextInput(
        attrs={"class": "layui-input", "id": "phone", "placeholder": "请输入手机号",
               "maxlength": "11", "lay-verify": "required|phone|regexit", "autofocus": "autofocus",
               "autocomplete": "off", "name": "mobile"}))
    password = forms.CharField(label="密码", max_length=20, widget=widgets.PasswordInput(
        attrs={"class": "layui-input", "id": "password", "placeholder": "请输入密码",
               "maxlength": "20", "lay-verify": "required|pwd",
               "autocomplete": "off", "autofocus": "autofocus", "name": "password"}))
    repassword = forms.CharField(label="确认密码", max_length=20, widget=widgets.PasswordInput(
        attrs={"class": "layui-input", "id": "repassword", "placeholder": "请再次输入密码",
               "maxlength": "20", "lay-verify": "required|repwd",
               "autocomplete": "off", "autofocus": "autofocus", "name": "repassword"}))
    mobile_captcha = forms.CharField(label="手机验证码", widget=widgets.TextInput(
        attrs={"class": "layui-input", "id": "msg-code", "placeholder": "请输入短信验证码", "maxlength": "6",
               "lay-verify": "required|number|msgcode"}))

    def clean_username(self):
        ret = User.objects.filter(username=self.cleaned_data.get("username"))
        if not ret:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名已注册")

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("repassword"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")


class ChangepwdForm(forms.Form):
    mobile = forms.CharField(label="手机号", max_length=11, widget=widgets.TextInput(
        attrs={"class": "layui-input", "id": "phone", "placeholder": "请输入手机号",
               "maxlength": "11", "lay-verify": "required|phone|regexit", "autofocus": "autofocus",
               "autocomplete": "off", "name": "mobile"}))
    mobile_captcha = forms.CharField(label="手机验证码", widget=widgets.TextInput(
        attrs={"class": "layui-input", "id": "msg-code", "placeholder": "请输入短信验证码", "maxlength": "6",
               "lay-verify": "required"}))

    password = forms.CharField(label="密码", max_length=20, widget=widgets.PasswordInput(
        attrs={"class": "layui-input", "id": "password", "placeholder": "请输入密码",
               "maxlength": "20", "lay-verify": "required|pwd",
               "autocomplete": "off", "autofocus": "autofocus", "name": "password"}))
    repassword = forms.CharField(label="确认密码", max_length=20, widget=widgets.PasswordInput(
        attrs={"class": "layui-input", "id": "repassword", "placeholder": "请再次输入密码",
               "maxlength": "20", "lay-verify": "required|repwd",
               "autocomplete": "off", "autofocus": "autofocus", "name": "repassword"}))

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            raise ValidationError("手机号未注册")
        else:
            return self.cleaned_data.get("mobile")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("repassword"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")
