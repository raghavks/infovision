{% if data.has_previous %}
    <li><a href="?page={{ data.previous_page_number }}"><i class="fa fa-chevron-left" aria-hidden="true"></i></a></li>
{% else %}
    <li class="disabled"><span><i class="fa fa-chevron-left" aria-hidden="true"></i></span></li>
{% endif %}

{% if data.number|add:'-4' > 1 %}
    <li><a href="?page={{ data.number|add:'-5' }}">&hellip;</a></li>
{% endif %}

{% for i in data.paginator.page_range %}
    {% if data.number == i %}
        <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
    {% elif i > data.number|add:'-5' and i < data.number|add:'5' %}
        <li><a href="?page={{ i }}">{{ i }}</a></li>
    {% endif %}
{% endfor %}

{% if data.paginator.num_pages > data.number|add:'4' %}
    <li><a href="?page={{ data.number|add:'5' }}">&hellip;</a></li>
{% endif %}

{% if data.has_next %}
    <li><a href="?page={{ data.next_page_number }}"><i class="fa fa-chevron-right" aria-hidden="true"></i></a></li>
{% else %}
    <li class="disabled"><span><i class="fa fa-chevron-right" aria-hidden="true"></i></span></li>
{% endif %}

</ul>