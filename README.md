# Django
在models.py中创建文章字段
在views.py中写入视图函数
在index.html中引入视图函数


##form表单带有验证错误的模板

        <form class="ui error tiny form" action="{% url 'comment' article.id %}" method="post">
            {% csrf_token %}
            {% if form.errors %} 验证有错误
                <div class="ui error message">
                    {{ form.errors }} 错误信息的显示
                </div>
                {% for field in form %}
                    <div class="{{ field.errors|yesno:'error, ' }} field">
                        {{ field.label }} {{ field }} 使用django过滤器提醒有错误的输入
                    </div>
                {% endfor %}
            {% else %}
                {% for field in form %}正确的输入
                    <div class="field">
                        {{ field.label }} {{ field }}
                    </div>
                {% endfor %}
            {% endif %}
            <button type="submit" class="ui blue button">Click</button>
        </form>
