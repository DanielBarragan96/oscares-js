import json

input_str = """ACTOR IN A LEADING ROLE
AUSTIN BUTLER
Elvis
COLIN FARRELL
The Banshees of Inisherin
BRENDAN FRASER
The Whale
PAUL MESCAL
Aftersun
BILL NIGHY
Living

ACTOR IN A SUPPORTING ROLE
BRENDAN GLEESON
The Banshees of Inisherin
BRIAN TYREE HENRY
Causeway
JUDD HIRSCH
The Fabelmans
BARRY KEOGHAN
The Banshees of Inisherin
KE HUY QUAN
Everything Everywhere All at Once

ACTRESS IN A LEADING ROLE
CATE BLANCHETT
Tár
ANA DE ARMAS
Blonde
ANDREA RISEBOROUGH
To Leslie
MICHELLE WILLIAMS
The Fabelmans
MICHELLE YEOH
Everything Everywhere All at Once

ACTRESS IN A SUPPORTING ROLE
ANGELA BASSETT
Black Panther: Wakanda Forever
HONG CHAU
The Whale
KERRY CONDON
The Banshees of Inisherin
JAMIE LEE CURTIS
Everything Everywhere All at Once
STEPHANIE HSU
Everything Everywhere All at Once

ANIMATED FEATURE FILM
GUILLERMO DEL TORO'S PINOCCHIO
Guillermo del Toro, Mark Gustafson, Gary Ungar and Alex Bulkley
MARCEL THE SHELL WITH SHOES ON
Dean Fleischer Camp, Elisabeth Holm, Andrew Goldman, Caroline Kaplan and Paul Mezey
PUSS IN BOOTS: THE LAST WISH
Joel Crawford and Mark Swift
THE SEA BEAST
Chris Williams and Jed Schlanger
TURNING RED
Domee Shi and Lindsey Collins

CINEMATOGRAPHY
ALL QUIET ON THE WESTERN FRONT
James Friend
BARDO, FALSE CHRONICLE OF A HANDFUL OF TRUTHS
Darius Khondji
ELVIS
Mandy Walker
EMPIRE OF LIGHT
Roger Deakins
TÁR
Florian Hoffmeister

COSTUME DESIGN
BABYLON
Mary Zophres
BLACK PANTHER: WAKANDA FOREVER
Ruth Carter
ELVIS
Catherine Martin
EVERYTHING EVERYWHERE ALL AT ONCE
Shirley Kurata
MRS. HARRIS GOES TO PARIS
Jenny Beavan

DIRECTING
THE BANSHEES OF INISHERIN
Martin McDonagh
EVERYTHING EVERYWHERE ALL AT ONCE
Daniel Kwan and Daniel Scheinert
THE FABELMANS
Steven Spielberg
TÁR
Todd Field
TRIANGLE OF SADNESS
Ruben Östlund

DOCUMENTARY FEATURE FILM
ALL THAT BREATHES
Shaunak Sen, Aman Mann and Teddy Leifer
ALL THE BEAUTY AND THE BLOODSHED
Laura Poitras, Howard Gertler, John Lyons, Nan Goldin and Yoni Golijov
FIRE OF LOVE
Sara Dosa, Shane Boris and Ina Fichman
A HOUSE MADE OF SPLINTERS
Simon Lereng Wilmont and Monica Hellström
NAVALNY
Daniel Roher, Odessa Rae, Diane Becker, Melanie Miller and Shane Boris

DOCUMENTARY SHORT FILM
THE ELEPHANT WHISPERERS
Kartiki Gonsalves and Guneet Monga
HAULOUT
Evgenia Arbugaeva and Maxim Arbugaev
HOW DO YOU MEASURE A YEAR?
Jay Rosenblatt
THE MARTHA MITCHELL EFFECT
Anne Alvergue and Beth Levison
STRANGER AT THE GATE
Joshua Seftel and Conall Jones

FILM EDITING
THE BANSHEES OF INISHERIN
Mikkel E.G. Nielsen
ELVIS
Matt Villa and Jonathan Redmond
EVERYTHING EVERYWHERE ALL AT ONCE
Paul Rogers
TÁR
Monika Willi
TOP GUN: MAVERICK
Eddie Hamilton

INTERNATIONAL FEATURE FILM
ALL QUIET ON THE WESTERN FRONT
Germany
ARGENTINA, 1985
Argentina
CLOSE
Belgium
EO
Poland
THE QUIET GIRL
Ireland

MAKEUP AND HAIRSTYLING
ALL QUIET ON THE WESTERN FRONT
Heike Merker and Linda Eisenhamerová
THE BATMAN
Naomi Donne, Mike Marino and Mike Fontaine
BLACK PANTHER: WAKANDA FOREVER
Camille Friend and Joel Harlow
ELVIS
Mark Coulier, Jason Baird and Aldo Signoretti
THE WHALE
Adrien Morot, Judy Chin and Annemarie Bradley

MUSIC (ORIGINAL SCORE)
ALL QUIET ON THE WESTERN FRONT
Volker Bertelmann
BABYLON
Justin Hurwitz
THE BANSHEES OF INISHERIN
Carter Burwell
EVERYTHING EVERYWHERE ALL AT ONCE
Son Lux
THE FABELMANS
John Williams

MUSIC (ORIGINAL SONG)
APPLAUSE
from Tell It like a Woman; Music and Lyric by Diane Warren
HOLD MY HAND
from Top Gun: Maverick; Music and Lyric by Lady Gaga and BloodPop
LIFT ME UP
from Black Panther: Wakanda Forever; Music by Tems, Rihanna, Ryan Coogler and Ludwig Goransson; Lyric by Tems and Ryan Coogler
NAATU NAATU
from RRR; Music by M.M. Keeravaani; Lyric by Chandrabose
THIS IS A LIFE
from Everything Everywhere All at Once; Music by Ryan Lott, David Byrne and Mitski; Lyric by Ryan Lott and David Byrne

BEST PICTURE
ALL QUIET ON THE WESTERN FRONT
Malte Grunert, Producer
AVATAR: THE WAY OF WATER
James Cameron and Jon Landau, Producers
THE BANSHEES OF INISHERIN
Graham Broadbent, Pete Czernin and Martin McDonagh, Producers
ELVIS
Baz Luhrmann, Catherine Martin, Gail Berman, Patrick McCormick and Schuyler Weiss, Producers
EVERYTHING EVERYWHERE ALL AT ONCE
Daniel Kwan, Daniel Scheinert and Jonathan Wang, Producers
THE FABELMANS
Kristie Macosko Krieger, Steven Spielberg and Tony Kushner, Producers
TÁR
Todd Field, Alexandra Milchan and Scott Lambert, Producers
TOP GUN: MAVERICK
Tom Cruise, Christopher McQuarrie, David Ellison and Jerry Bruckheimer, Producers
TRIANGLE OF SADNESS
Erik Hemmendorff and Philippe Bober, Producers
WOMEN TALKING
Dede Gardner, Jeremy Kleiner and Frances McDormand, Producers

PRODUCTION DESIGN
ALL QUIET ON THE WESTERN FRONT
Production Design: Christian M. Goldbeck; Set Decoration: Ernestine Hipper
AVATAR: THE WAY OF WATER
Production Design: Dylan Cole and Ben Procter; Set Decoration: Vanessa Cole
BABYLON
Production Design: Florencia Martin; Set Decoration: Anthony Carlino
ELVIS
Production Design: Catherine Martin and Karen Murphy; Set Decoration: Bev Dunn
THE FABELMANS
Production Design: Rick Carter; Set Decoration: Karen O'Hara

SHORT FILM (ANIMATED)
THE BOY, THE MOLE, THE FOX AND THE HORSE
Charlie Mackesy and Matthew Freud
THE FLYING SAILOR
Amanda Forbis and Wendy Tilby
ICE MERCHANTS
João Gonzalez and Bruno Caetano
MY YEAR OF DICKS
Sara Gunnarsdóttir and Pamela Ribon
AN OSTRICH TOLD ME THE WORLD IS FAKE AND I THINK I BELIEVE IT
Lachlan Pendragon

SHORT FILM (LIVE ACTION)
AN IRISH GOODBYE
Tom Berkeley and Ross White
IVALU
Anders Walter and Rebecca Pruzan
LE PUPILLE
Alice Rohrwacher and Alfonso Cuarón
NIGHT RIDE
Eirik Tveiten and Gaute Lid Larssen
THE RED SUITCASE
Cyrus Neshvad

SOUND
ALL QUIET ON THE WESTERN FRONT
Viktor Prášil, Frank Kruse, Markus Stemler, Lars Ginzel and Stefan Korte
AVATAR: THE WAY OF WATER
Julian Howarth, Gwendolyn Yates Whittle, Dick Bernstein, Christopher Boyes, Gary Summers and Michael Hedges
THE BATMAN
Stuart Wilson, William Files, Douglas Murray and Andy Nelson
ELVIS
David Lee, Wayne Pashley, Andy Nelson and Michael Keller
TOP GUN: MAVERICK
Mark Weingarten, James H. Mather, Al Nelson, Chris Burdon and Mark Taylor

VISUAL EFFECTS
ALL QUIET ON THE WESTERN FRONT
Frank Petzold, Viktor Müller, Markus Frank and Kamil Jafar
AVATAR: THE WAY OF WATER
Joe Letteri, Richard Baneham, Eric Saindon and Daniel Barrett
THE BATMAN
Dan Lemmon, Russell Earl, Anders Langlands and Dominic Tuohy
BLACK PANTHER: WAKANDA FOREVER
Geoffrey Baumann, Craig Hammack, R. Christopher White and Dan Sudick
TOP GUN: MAVERICK
Ryan Tudhope, Seth Hill, Bryan Litson and Scott R. Fisher

WRITING (ADAPTED SCREENPLAY)
ALL QUIET ON THE WESTERN FRONT
Screenplay - Edward Berger, Lesley Paterson & Ian Stokell
GLASS ONION: A KNIVES OUT MYSTERY
Written by Rian Johnson
LIVING
Written by Kazuo Ishiguro
TOP GUN: MAVERICK
Screenplay by Ehren Kruger and Eric Warren Singer and Christopher McQuarrie; Story by Peter Craig and Justin Marks
WOMEN TALKING
Screenplay by Sarah Polley

WRITING (ORIGINAL SCREENPLAY)
THE BANSHEES OF INISHERIN
Written by Martin McDonagh
EVERYTHING EVERYWHERE ALL AT ONCE
Written by Daniel Kwan & Daniel Scheinert
THE FABELMANS
Written by Steven Spielberg & Tony Kushner
TÁR
Written by Todd Field
TRIANGLE OF SADNESS
Written by Ruben Östlund
"""

def parse_data(input_str):
    output = []
    categories = []
    current_category = ""
    current_nominees = []
    current_nominee = "";
    ended = True

    # Split the input string by line breaks
    lines = input_str.split('\n')

    # Loop through each line
    for line in lines:
        if ended:
            current_category = line
            current_nominees = []
            ended = False
        # If the line is empty, skip it
        elif not line:
            categories.append({"title": current_category, "nominees": current_nominees})
            ended = True
            continue
        # Otherwise, the line is a nominee
        elif current_nominee == "":
            current_nominee = line
        else:
            current_nominee += ", " + line
            current_nominees.append(current_nominee)
            current_nominee = ""

    # Add the last category to the output
    categories.append({"title": current_category, "nominees": current_nominees})

    return categories



res = parse_data(input_str)
res_string = json.dumps(res, ensure_ascii=False).encode('utf8')
text_file = open("nominations.json", "w", encoding='utf-8')
n = text_file.write(json.dumps(res, ensure_ascii=False))
text_file.close()

