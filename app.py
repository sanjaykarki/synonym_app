from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Datamuse API
API_URL = "https://api.datamuse.com/words?rel_syn="


def get_synonyms(word):
    """
    Function to get synonyms of a given word from Datamuse API
    :param word: str, word to get synonyms of
    :return: tuple, (list of synonyms, error message)
    """
    url = f'{API_URL}{word}'
    try:
        response = requests.get(url)
        # Extracting first 10 synonyms from the response
        synonyms = response.json()[:10]

        # Checking if synonyms were found
        if not synonyms:
            return None, 'No synonyms found for the given word.'
        return synonyms, None
    except requests.exceptions.RequestException as e:
        return None, "Couldn't connect to API or internet."


@app.route('/', methods=['GET', 'POST'])
def synonym_app():
    """
    Flask route to handle the synonym app
    :return: rendered template
    """
    if request.method == 'POST':
        word = request.form.get('word')

        # Checking if word is provided
        if not word:
            return render_template('index.html', error='Please provide a word.')

        synonyms, error = get_synonyms(word)

        # Checking if error occurred
        if error:
            return render_template('index.html', error=error)

        return render_template('index.html', synonyms=synonyms)

    # Returning the template for GET request
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
