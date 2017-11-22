{% extends "base_generic.html" %}
{% block content %}
    <h1>Your Home Price Estimation</h1>
    
    <ul>
        
        <li>
            <a href =""> {{ price|floatformat:2 }} NIS </a>
        </li>
        
    </ul>
    
        
    
{% endblock %}    
