# str = input("请输入：")
# if 'EUR 1.409,00' in str:
#     print(str[4]+str[6]+str[7]+str[8])
# elif '$ 409,05' in str:
#     a = str.replace(',', '.')
#     print(a[2::])
# elif '￥409.50' in str:
#     print(str[1:6])
# elif 'CNY 1,000' in str:
#     b = str.replace(',', '')
#     print(b[4::])
# else:
#     print("输入有误")
#
#
# $(function () {
#     $.get( "test.php", function( data ) {
#         $( "body" ).prepend( "aaa" );
#     });
#     $("body").append("bbb");
# });
#
#
#
# class User
# {
#     public $username;
#
#     public function __construct(string $username)
#     {
#         $this->username = $username;
#     }
# }
#
# $users = [
#     new User('user 1'),
#     new User('user 2'),
#     new User('user 3'),
# ];
#
# var_dump(array_map("__construct", $users));
#
#
import sys,time
start = time.clock()
try:
    a = int(input('请输入整数a:'))
    if a >= -5*10^4:
        b = int(input('请输入整数b:'))
    else:
        sys.exit()
    if b <= 5*10^4 and b >= a:
        c = int(input('请输入正整数c:'))
    else:
        sys.exit()
    if c >= 1 and c <= 500:
        print("请稍等!")
    else:
        sys.exit()
except:
    print("请重新输入,注意:a为整数,b为整数,b比a大,c为正整数!")

d = 0
for i in range(a, b+1):
    if i % c == 0:
        d = d+1
print("一共有"+str(d)+"个数满足条件")
end = time.clock()
print("共耗时:" + str(end-start))
