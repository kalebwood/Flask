from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #everytime we make a change, it automatically reruns the webserver (True for testing, False for Production)
    