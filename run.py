from app import init_app

if __name__ == '__main__':
    app = init_app()
    app.run(host='0.0.0.0')
