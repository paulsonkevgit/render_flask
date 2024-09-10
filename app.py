from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = [
            {
                'name': 'IRON MAN',
                'cast': 'Robert Downey Jr, Gwyneth Paltrow',
                'crew': {'director': 'John Favreau', 'producer': 'Kevin Feige'},
                'image': 'IRONMAN.jpg',
                'story_outline': 'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.',
                'trailer_url': 'https://www.youtube.com/watch?v=8ugaeA-nMTc',  # Replace with actual trailer URL
                'release_year': 2008
            },
            {
                'name': 'THE INCREDIBLE HULK',
                'cast': 'Edward Norton, Liv Tyler',
                'crew': {'director': 'Louis Leterrier', 'producer': 'Kevin Feige'},
                'image': 'TheIncredibleHulk.jpg',
                'story_outline': 'Bruce Banner, on the run from the U.S. government, must find a cure for his gamma radiation exposure while evading the pursuit of the ruthless General Thaddeus Ross.',
                'trailer_url': 'https://www.youtube.com/watch?v=xbqNb2PFKKA',  # Replace with actual trailer URL
                'release_year': 2008
            },
            {
                'name': 'IRON MAN 2',
                'cast': 'Robert Downey Jr, Gwyneth Paltrow, Don Cheadle',
                'crew': {'director': 'Jon Favreau', 'producer': 'Kevin Feige'},
                'image': 'IronMan2.jpg',
                'story_outline': 'Tony Stark faces pressure from the government and rival industries while dealing with his declining health. Meanwhile, a new threat emerges in the form of Ivan Vanko, seeking revenge against Stark.',
                'trailer_url': 'https://www.youtube.com/watch?v=qsRZghNciIo',  # Replace with actual trailer URL
                'release_year': 2010
            },
            {
                'name': 'THOR',
                'cast': 'Chris Hemsworth, Natalie Portman',
                'crew': {'director': 'Kenneth Branagh', 'producer': 'Kevin Feige'},
                'image': 'Thor.jpg',
                'story_outline': 'Banished to Earth, Thor, the Norse God of Thunder, must learn humility and wield his enchanted hammer, Mjolnir, to save both Asgard and humanity from his power-hungry brother, Loki.',
                'trailer_url': 'https://www.youtube.com/watch?v=JOddp-nlNvQ',  # Replace with actual trailer URL
                'release_year': 2011
            },
            {
                'name': 'CAPTAIN AMERICA: THE FIRST AVENGER',
                'cast': 'Chris Evans, Hayley Atwell',
                'crew': {'director': 'Joe Johnston', 'producer': 'Kevin Feige'},
                'image': 'CaptainAmericaTheFirstAvenger.jpg',
                'story_outline': 'During World War II, Steve Rogers undergoes an experiment that transforms him into Captain America. He battles the evil HYDRA organization led by the Red Skull, armed with a vibranium shield.',
                'trailer_url': 'https://www.youtube.com/watch?v=JerVrbLldXw',  # Replace with actual trailer URL
                'release_year': 2011
            },
            {
                'name': 'THE AVENGERS',
                'cast': 'Robert Downey Jr, Chris Evans, Chris Hemsworth, Scarlett Johansson, Mark Ruffalo, Jeremy Renner',
                'crew': {'director': 'Joss Whedon', 'producer': 'Kevin Feige'},
                'image': 'TheAvengers.jpg',
                'story_outline': 'Nick Fury of S.H.I.E.L.D. brings together a team of superheroes, including Iron Man, Captain America, Thor, Hulk, Black Widow, and Hawkeye, to stop Thor\'s adoptive brother Loki from enslaving humanity.',
                'trailer_url': 'https://www.youtube.com/watch?v=eOrNdBpGMv8',  # Replace with actual trailer URL
                'release_year': 2012
            }
        ]
        print("Request received successfully")
        return jsonify(movies)
    except Exception as e:
        print(f"Error in get_movies: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/images/<filename>')
def get_image(filename):
    try:
        return send_from_directory('images', filename)
    except Exception as e:
        print(f"Error in get_image: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', debug=True)
