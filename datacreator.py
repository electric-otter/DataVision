# Input data and write to file
temp = input("Please enter your data!! ")
try:
    with open('data.txt', 'w') as gfg:
        gfg.write(temp)  # Write the input data to the file
    print("Data has been saved. Launching server...")
except Exception as e:
    print("There is a problem:", str(e))

# Import necessary modules for Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to load data from the file
def load_data():
    try:
        with open('data.txt', 'r') as f:
            data = f.read().splitlines()  # Read each line as an individual item
        return data
    except Exception as e:
        print("Error loading data:", str(e))
        return []

# Data storage (load data from file)
data = load_data()

# Function to display the data
@app.route('/')
def index():
    return render_template('data.html', data=data)

# Function to delete an item from the list
@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    global data
    if 0 <= item_id < len(data):
        data.pop(item_id)  # Remove the item at the specified index
        # Write the updated list back to the file
        with open('data.txt', 'w') as f:
            f.write("\n".join(data))
    return redirect(url_for('index'))  # Redirect back to the index page

if __name__ == '__main__':
    app.run(debug=True)
