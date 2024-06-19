from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key'
users = {'user1': 'password1', 'user2': 'password2'}

print("This is a music making tutorial website.")

@app.route('/')
def home():
    if 'username' in session:
        return'''
        <font color="#4169E1"><h2>Welcome to this music making tutorial website!</h2></font>
        <font color="#4169E1"><h2>Start your journey of music!</h2></font>
        <a href="/before_start">Before Start</a>
        <a href="/tutorial">Tutorial</a>
        <a href="/about_us">About Us</a>
        '''
    return redirect(url_for('login'))

@app.route("/tutorial")
def tutorial():
    return'''
    <font color="#4169E1"><h1>Tutorial</h1></font>
    <h2>Contents</h2>
    <details>
    <summary>Basic Knowledge</summary>
    <p><a href="http://127.0.0.1:5000/basic_knowledge/rhythm">Rhythm</a></p>
    <p><a href="http://127.0.0.1:5000/basic_knowledge/pitch">Notes, Pitch and Key</a></p>
    <p><a href="http://127.0.0.1:5000/basic_knowledge/chord">Chord</a></p>
    </details>
    <details>
    <summary>Style Features</summary>
    <p><a href="http://127.0.0.1:5000/style_features/jazz">Jazz</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/rock">Rock</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/classical">Classical</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/edm">EDM</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/pop">Pop</a></p>
    </details>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/about_us")
def about_us():
    return'''
    <font color="#4169E1"><h1>About Us</h1></font>
    <font color="#2CC7AC"><h3>Author: Alpha122</h3></font>
    <h3><a href="https://x.com/Alpha638224">Twitter: Alpha122</a></h3>
    <font color="#2CC7AC"><h3>Discord: Alpha122#9584</h3></font>
    <font color="#2CC7AC"><h3>Instagram: Alpha638224</h3></font>
    <p>The purpose of building this website is to let more music lovers are able to start learning how to make music from the beginning,</p>
    <p>Even they have nothing on music. For pros, you can also find style features information here, which might also help you as well.</p>
    <p>If you have any suggestions, welcome to contact the author.</p>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/before_start")
def before_start():
    return'''
    <font color="#4169E1"><h1>Before Start</h1></font>
    <h2>Introduction</h2>
    <p>Making music is not a thing far away from us, everyone who loves music can make it, as long as you stick to your own path, nothing can stop you. Let’s immersed in the world of music, enjoy the beautifulness of notes!</p>
    <h2>What is music making?</h2>
    <p>Unlike traditional composition, music making is making music in DAW(Music Making Software) which allows you to select different instrument for every track, even vocals or cool samples.</p>
    <h2>Software Recommendation</h2>
    <font color="#4169E1"><h3>Different software works for different systems, please choose a software according to your devices.</h3></font>
    <font color="#2CC7AC"><h3>iOS：Medly、Garage Band、FLM、Auxy</h3></font>
    <font color="#2CC7AC"><h3>Android：FLM</h3></font>
    <font color="#2CC7AC"><h3>MacOS：Logic Pro、Cubase</h3></font>
    <font color="#2CC7AC"><h3>Windows：FL Studio、Cubase、Abelton Live</h3></font>
    <font color="#E77B55"><h3>Vocal Generating Software：ACE Studio, Vocaloid, Synthesizer V</h3></font>
    <h2>Preparation before we start</h2>
    <p>If you want to start making music, you have to know the basic knowledge of music theory and how to use the software.</p>
    <p>For example, you have to know at least triads, simple melodies and rhythms, and also how to write notes in, adjust parameters and export audio in the software of your choice. With these in hand, you can try to make your first song!</p>
    <p>Before you start, you can think of what styles of music you usually listen to, then choose one you like the most, such as EDM, Vocaloid Songs, J-pop, K-pop, C-pop, EA-pop, Folk, Symphony, Jazz, Classical, etc.</p>
    <p>Each music style has different BPM, style features, instrument selection and difficulty.</p>
    <h2>Listening to music</h2>
    <p>For ordinary people, listening to music is a way of relaxation, but for music makers, listening to music is also an effective way to increase your level on music making. Listen to good songs and try to analyze and deconstruct it with what you've learned.</p>
    <p>When you reach a higher level, you will even be able to directly know the chord progression and other elements of any songs, and even give them a critical and accurate evaluation. You'll also have the ability to distinguish good songs and bad songs, and decide what kind of songs are worth staying in your playlist.</p>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/basic_knowledge/rhythm")
def rhythm():
    return'''
    <h1>Rhythm</h1>
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/basic_knowledge/pitch")
def Pitch():
    return'''
    <h1>Notes, Pitch and Key</h1>
    <p>There're 12 different notes in a single octave, each note has different pitch.</p>
    <p>They're C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A ,A#/Bb, B.</p>
    <p>Each of them also have a solfege, which are do, ra, re, me, mi, fa, fi, so, le, la, te, ti.</p>
    <p>Regard each of them as 1(do), and both of them has major and minor key, you'll get 24 keys in total.</p>
    <p>When you're singing or remembering melodies, you always using their solfege instead of their pitch.</p>
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/basic_knowledge/chord")
def Chord():
    return'''
    <h1>Chord</h1>
    <font color="#2CC7AC"><h3>Chord is a group of three or more notes played simultaneously.</h3></font>
    <h2>Chord types</h2>
    <details>
    <summary>Triads</summary>
    <p><a href="http://127.0.0.1:5000/basic_knowledge/chord/major_triads">Major Triads</a></p>
    <p><a href="http://127.0.0.1:5000/basic_knowledge/chord/minor_triads">Minor Triads</a></p>
    <font color="#4169E1"><p>Diminished Triads</p></font>
    <font color="#4169E1"><p>Augumented Triads</p></font>
    </details>
    <details>
    <summary>Seventh Chord</summary>
    <font color="#4169E1"><p>Major-Major Seventh</p></font>
    <font color="#4169E1"><p>Major-Minor Seventh</p></font>
    <font color="#4169E1"><p>Minor-Minor Seventh</p></font>
    <font color="#4169E1"><p>Diminished Seventh</p></font>
    <font color="#4169E1"><p>Half Diminished Seventh</p></font>
    </details>
    <details>
    <summary>Ninth Chord</summary>
    <font color="#4169E1"><p>Major Ninth</p></font>
    <font color="#4169E1"><p>Minor Ninth</p></font>
    </details>
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/basic_knowledge/chord/major_triads")
def Major_triads():
    return'''
    <h1>Major Triads</h1>
    Major triads are triads which consist of a major third and a minor third.
    It usually brings a delightful and positive feeling on listening.
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/basic_knowledge/chord/minor_triads")
def Minor_triads():
    return'''
    <h1>Minor Triads</h1>
    Minor triads are triads which consist of a minor third and a major third.
    It usually brings a sorrow and sad feeling on listening.
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/style_features/jazz")
def Jazz():
    return'''
    <h1>Jazz</h1>
    Jazz is a music genre that originated in the African-American communities of New Orleans, Louisiana, in the late 19th and early 20th centuries, with its roots in blues, ragtime, European harmony and African rhythmic rituals.
    Since the 1920s Jazz Age, it has been recognized as a major form of musical expression in traditional and popular music. Jazz is characterized by swing and blue notes, complex chords, call and response vocals, polyrhythms and improvisation.
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/style_features/rock")
def Rock():
    return'''
    <h1>Rock</h1>
    Rock is a broad genre of popular music that originated as “rock and roll” in the United States in the late 1940s and early 1950s, developing into a range of different styles from the mid-1960s, particularly in the United States and the United Kingdom.
    It has its roots in 1940s and 1950s rock and roll, a style that drew directly from the blues and rhythm and blues genres of African-American music and from country music.
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/style_features/classical")
def Classical():
    return'''
    <h1>Classical</h1>
    Classical music generally refers to the art music of the Western world, considered to be distinct from Western folk music or popular music traditions.
    It is sometimes distinguished as Western classical music, as the term "classical music" can also be applied to non-Western art musics.
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/style_features/edm")
def EDM():
    return'''
    <h1>EDM</h1>
    Electronic dance music (EDM) is a broad range of percussive electronic music genres originally made for nightclubs, raves, and festivals. It is generally produced for playback by DJs who create seamless selections of tracks, called a DJ mix, by segueing from one recording to another.
    EDM producers also perform their music live in a concert or festival setting in what is sometimes called a live PA. Since its inception EDM has expanded to include a wide range of subgenres.
    <p>EDM has over 120 sub-styles, which makes it an incredibly colorful music style, that's a main reason that youth like them so much.</p>
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/style_features/pop")
def Pop():
    return'''
    <h1>Pop</h1>
    Pop music is a genre of popular music that originated in its modern form during the mid-1950s in the United States and the United Kingdom. During the 1950s and 1960s, pop music encompassed rock and roll and the youth-oriented styles it influenced.
    Rock and pop music remained roughly synonymous until the late 1960s, after which pop became associated with music that was more commercial, ephemeral, and accessible.
    <details>
    <summary>Pop types</summary>
    <p><a href="http://127.0.0.1:5000/style_features/pop/ea_pop">EA-pop</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/pop/j_pop">J-pop</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/pop/c_pop">C-pop</a></p>
    <p><a href="http://127.0.0.1:5000/style_features/pop/k_pop">K-pop</a></p>
    </details>
    <h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
    <h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
    '''

@app.route("/style_features/pop/ea_pop")
def EA_pop():
    return'''
<h1>EA-pop</h1>
'''

@app.route("/style_features/pop/j_pop")
def J_pop():
    return'''
<h1>J-pop</h1>
J-pop (Japanese: ジェーポップ, often stylized in all caps; an abbreviated form of "Japanese popular music or Japanese Pop Music"), natively also known simply as pops (ポップス, poppusu), is the name for a form of popular music that entered the musical mainstream of Japan in the 1990s. Modern J-pop has its roots in traditional music of Japan, and significantly in 1960s pop and rock music. J-pop replaced kayokyoku ("Lyric Singing Music", a term for Japanese popular music from the 1920s to the 1980s) in the Japanese music scene.
<h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
<h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
'''

@app.route("/style_features/pop/c_pop")
def C_pop():
    return'''
<h1>C-pop</h1>
C-pop is an abbreviation for Chinese popular music (traditional Chinese: 漢語流行音樂; simplified Chinese: 汉语流行音乐), a loosely defined musical genre by artists originating from mainland China, Hong Kong and Taiwan (the Greater China region). This also includes countries where Chinese languages are used by parts of the population, such as Singapore and Malaysia. C-pop is used as an umbrella term covering not only Chinese pop but also R&B, ballads, Chinese rock, Chinese hip hop and Chinese ambient music, although Chinese rock diverged during the early 1990s.
<h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
<h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
'''

@app.route("/style_features/pop/k_pop")
def K_pop():
    return'''
<h1>K-pop</h1>
K-pop (Korean: 케이팝; RR: keipap), short for Korean popular music, is a form of popular music originating in South Korea as part of South Korean culture. It includes styles and genres from around the world, such as pop, hip hop, R&B, rock, jazz, gospel, reggae, electronic dance, folk, country, disco, and classical on top of its traditional Korean music roots.
The term "K-pop" became popular in the 2000s, especially in the international context. The Korean term for domestic pop music is gayo (가요; 歌謠), which is still widely used within South Korea. While "K-pop" can refer to all popular music or pop music from South Korea, it is colloquially often used in a narrower sense for any Korean music and artists associated with the entertainment and idol industry in the country, regardless of the genre.
<h3><a href="http://127.0.0.1:5000/tutorial">Back to tutorial page</a></h3>
<h3><a href="http://127.0.0.1:5000/">Back to home page</a></h3>
'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    available_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                            '0','1','2','3','4','5','6','7','8','9','_']
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        a = 0
        b = 0
        valid = True
        for i in range(len(password)):
            for i in range(65):
                if password[b] in available_characters:
                    valid = True
                    break
                else:
                    a += 1
                    valid = False
            if valid == True:
                b += 1
            else:
                return '''Your password can only consist of letters, numbers and "_".
                <a href="/register">Retry</a>'''
        a = 0
        b = 0
        valid = True
        for i in range(len(username)):
            for i in range(65):
                if username[b] in available_characters:
                    valid = True
                    break
                else:
                    a += 1
                    valid = False
            if valid == True:
                b += 1
            else:
                return '''Your username can only consist of letters, numbers and "_".
                <a href="/register">Retry</a>'''
        if len(password) < 8:
            return '''Your password is too short! A valid password should be at least 8 characters long.
            <a href="/register">Retry</a>'''
        if len(username) < 8:
            return '''Your username is too short! A valid username should be at least 8 characters long.
            <a href="/register">Retry</a>'''
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        return '''This username has been already registered, please choose another username.
            <a href="/register">Retry</a>'''
    
    return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Register</title>
    </head>
    <body>
        <h1>Register</h1>
        <form action="/register" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Register">
        </form>
    </body>
    </html>'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return '''<p>Incorrect password or user name.</p>
            <a href="/login">Retry</a>'''
    
    return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
    </head>
    <body>
        <h1>Login</h1>
        <form action="/login" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    </body>
    <a href="/register">Don't have an account? Register here</a>
    </html>'''

if __name__ == '__main__':
    app.run()