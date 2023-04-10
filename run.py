from market import app

# Checks if the run.py file has been executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
