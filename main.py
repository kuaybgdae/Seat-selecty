{% load static %}
<!DOCTYPE html>
<html>
<head>
	<title>Home Page</title>
    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
</head>
<body>
    <div class="container">
        <!-- Your content goes here -->
    </div>
	<h1>Welcome to the Home Page</h1>
	<p>You have successfully logged in!</p>
	<div>
		<li><a href="{% url 'ticket' %}">购买机票</a></li>
	</div>
	<div>
        <li><a href="{% url 'order' %}">查看订单</a></li>
	</div>
    <div>
        <li><a href="{% url 'user_passage' %}">查看用户信息</a></li>
	</div>
</body>
</html>
