# -*- coding: utf8 -*-
# we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently
# we can obtain test cases from test management tools, I used this for my previous project: http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx
# We can also record the result of test cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['0','Low', 'when user goes to main page, page should be loaded'],
    ['1','Normal', 'In Main page, when user search "pin dell insprison3537" button, he should see result for "62 items"'],
    ['2','Normal', 'In Main page, when user click "Sing up" button, he should see Sign up Page'],
    ['3','High', 'In Main page, when user click "Sing in" button, he should see Sign in Page'],
    ['4','Normal', 'In Login Page, when user login with a empty email, right password, he should see Error Message: "Vui lòng nhập Email hoặc Số điện thoại"'],
    ['5','Normal', 'In Login Page, when user login with a right email, empty password, he should see Error Message: "Mật khẩu không chính xác"'],
    ['6','Normal', 'In Login Page, when user login with a empty email, empty password he should see Error Message: "Vui lòng nhập Email hoặc Số điện thoại"'],
    ['7','Normal', 'In Login Page, when user login with a in-valid email, right password he should see Error Message: "Số điện thoại không hợp lệ"'],
    ['8','Normal', 'In Login Page, when user login with a right email, wrong password he should see Error Message: "Mật khẩu không chính xác"'],
    ['9','Low', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['10','Normal', 'when user goes to main page, the title of page is Shopping online - Buy online on Lazada.vn'],
    ['11','Normal', 'In Main page, when user click CUSTOMEMR CARE, he should see Customer Care page'],
    ['12', 'Normal', 'In Cart page, when user click  choose an item, he should see that item in Cart Page'],
    ['13', 'Normal', 'In Cart page, when user click delete an item, he should not see that item in Cart Page']
]