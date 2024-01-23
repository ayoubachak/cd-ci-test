from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

@app.route('/hello/<name>')
def hello(name):
    """
    A dynamic route that greets the user by name.

    This route demonstrates the use of dynamic URL parameters in Flask. When a user accesses
    this route, the 'name' part of the URL is dynamic, meaning it can change. Whatever value
    is placed in '<name>' will be passed to this function and used in the greeting.

    The function returns a personalized greeting message with the provided name.

    Args:
        name (str): A dynamic part of the URL. It's the name of the person to greet.

    Returns:
        str: A greeting message, which includes the name provided in the URL.

    Example:
        Accessing this URL - http://[your_server_address]/hello/John
        will result in the response - "Hello, John!"

    Note:
        The route by default only handles GET requests. If needed, modify the route
        decorator to handle other HTTP methods (e.g., methods=['GET', 'POST']).
    """

    # Return a formatted string with the provided name
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
