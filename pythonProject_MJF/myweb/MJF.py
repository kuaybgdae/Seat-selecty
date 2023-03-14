{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>个人信息管理</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/user_passage.css' %}">
</head>
<body>
	<div class="container">
		<h1>个人信息</h1>
		<form method="post">
			{% csrf_token %}
			<div class="form-group">
				<label for="from">姓名：</label>
				<input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="form-group">
				<label for="from">用户名：</label>
				<input type="text" class="form-control" id="username" name="username">
			</div>
			<div class="form-group">
			<label for="gender">性别：</label>
			<select class="form-control" id="gender" name="gender">
				<option value="男">男</option>
				<option value="女">女</option>
			</div>
			<div class="form-group">
			    <label for="phone">电话号码：</label>
				<input type="text" class="form-control" id="phone" name="phone" pattern="[0-9]{11}" placeholder="请输入11位电话号码">
			</div>
			<div class="form-group">
				<label for="birthday">生日：</label>
				<input type="date" class="form-control" id="birthday" name="birthday">
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input type="password" class="form-control" id="password" name="password">
			</div>

			<div class="form-group">
				<label for="to">座位偏好设置：</label>
				<select class="form-control" id="to" name="to">
					<option value="">靠前靠窗</option>
					<option value="">靠中靠窗</option>
					<option value="">靠后靠窗</option>
					<option value="">靠前不靠窗</option>
					<option value="">靠中不靠窗</option>
					<option value="">靠后不靠窗</option>
				</select>
			</div>
			<div class="form-group">
				<label for="time">证件信息：</label>
				<select class="form-control" id="time" name="time">
					<option value="身份证">身份证</option>
					<option value="居民证">居民证</option>
					<option value="其他证件">其他证件</option>
				</select>
			</div>
			<button type="submit" class="btn btn-primary">修改</button>
			<button type="button" class="btn btn-secondary" onclick="location.href='{% url 'home' %}'">返回</button>
		</form>
	</div>


	<script src="{% static 'js/user_passage.js' %}"></script>
</body>
</html>




