import json

input_str = """ACTOR IN A LEADING ROLE
BRADLEY COOPER
Maestro
COLMAN DOMINGO
Rustin
PAUL GIAMATTI
The Holdovers
CILLIAN MURPHY
Oppenheimer
JEFFREY WRIGHT
American Fiction

ACTOR IN A SUPPORTING ROLE
STERLING K. BROWN
American Fiction
ROBERT DE NIRO
Killers of the Flower Moon
ROBERT DOWNEY JR.
Oppenheimer
RYAN GOSLING
Barbie
MARK RUFFALO
Poor Things

ACTRESS IN A LEADING ROLE
ANNETTE BENING
Nyad
LILY GLADSTONE
Killers of the Flower Moon
SANDRA HÜLLER
Anatomy of a Fall
CAREY MULLIGAN
Maestro
EMMA STONE
Poor Things

ACTRESS IN A SUPPORTING ROLE
NOMINEES
EMILY BLUNT
Oppenheimer
DANIELLE BROOKS
The Color Purple
AMERICA FERRERA
Barbie
JODIE FOSTER
Nyad
DA'VINE JOY RANDOLPH
The Holdovers

ANIMATED FEATURE FILM
THE BOY AND THE HERON
Hayao Miyazaki and Toshio Suzuki
ELEMENTAL
Peter Sohn and Denise Ream
NIMONA
Nick Bruno, Troy Quane, Karen Ryan and Julie Zackary
ROBOT DREAMS
Pablo Berger, Ibon Cormenzana, Ignasi Estapé and Sandra Tapia Díaz
SPIDER-MAN: ACROSS THE SPIDER-VERSE
Kemp Powers, Justin K. Thompson, Phil Lord, Christopher Miller and Amy Pascal

CINEMATOGRAPHY
EL CONDE
Edward Lachman
KILLERS OF THE FLOWER MOON
Rodrigo Prieto
MAESTRO
Matthew Libatique
OPPENHEIMER
Hoyte van Hoytema
POOR THINGS
Robbie Ryan

COSTUME DESIGN
BARBIE
Jacqueline Durran
KILLERS OF THE FLOWER MOON
Jacqueline West
NAPOLEON
Janty Yates and Dave Crossman
OPPENHEIMER
Ellen Mirojnick
POOR THINGS
Holly Waddington

DIRECTING
ANATOMY OF A FALL
Justine Triet
KILLERS OF THE FLOWER MOON
Martin Scorsese
OPPENHEIMER
Christopher Nolan
POOR THINGS
Yorgos Lanthimos
THE ZONE OF INTEREST
Jonathan Glazer

DOCUMENTARY FEATURE FILM
BOBI WINE: THE PEOPLE'S PRESIDENT
Moses Bwayo, Christopher Sharp and John Battsek
THE ETERNAL MEMORY
FOUR DAUGHTERS
Kaouther Ben Hania and Nadim Cheikhrouha
TO KILL A TIGER
Nisha Pahuja, Cornelia Principe and David Oppenheim
20 DAYS IN MARIUPOL
Mstyslav Chernov, Michelle Mizner and Raney Aronson-Rath

DOCUMENTARY SHORT FILM
THE ABCS OF BOOK BANNING
Sheila Nevins and Trish Adlesic
THE BARBER OF LITTLE ROCK
John Hoffman and Christine Turner
ISLAND IN BETWEEN
S. Leo Chiang and Jean Tsien
THE LAST REPAIR SHOP
Ben Proudfoot and Kris Bowers
NǍI NAI & WÀI PÓ
Sean Wang and Sam Davis

FILM EDITING
ANATOMY OF A FALL
Laurent Sénéchal
THE HOLDOVERS
Kevin Tent
KILLERS OF THE FLOWER MOON
Thelma Schoonmaker
OPPENHEIMER
Jennifer Lame
POOR THINGS
Yorgos Mavropsaridis

INTERNATIONAL FEATURE FILM
IO CAPITANO
Italy
PERFECT DAYS
Japan
SOCIETY OF THE SNOW
Spain
THE TEACHERS' LOUNGE
Germany
THE ZONE OF INTEREST
United Kingdom

MAKEUP AND HAIRSTYLING
GOLDA
Karen Hartley Thomas, Suzi Battersby and Ashra Kelly-Blue
MAESTRO
Kazu Hiro, Kay Georgiou and Lori McCoy-Bell
OPPENHEIMER
Luisa Abel
POOR THINGS
Nadia Stacey, Mark Coulier and Josh Weston
SOCIETY OF THE SNOW
Ana López-Puigcerver, David Martí and Montse Ribé

MUSIC (ORIGINAL SCORE)
AMERICAN FICTION
Laura Karpman
INDIANA JONES AND THE DIAL OF DESTINY
John Williams
KILLERS OF THE FLOWER MOON
Robbie Robertson
OPPENHEIMER
Ludwig Göransson
POOR THINGS
Jerskin Fendrix

MUSIC (ORIGINAL SONG)
THE FIRE INSIDE
from Flamin' Hot; Music and Lyric by Diane Warren
I'M JUST KEN
from Barbie; Music and Lyric by Mark Ronson and Andrew Wyatt
IT NEVER WENT AWAY
from American Symphony; Music and Lyric by Jon Batiste and Dan Wilson
WAHZHAZHE (A SONG FOR MY PEOPLE)
from Killers of the Flower Moon; Music and Lyric by Scott George
WHAT WAS I MADE FOR?
from Barbie; Music and Lyric by Billie Eilish and Finneas O'Connell

BEST PICTURE
AMERICAN FICTION
Ben LeClair, Nikos Karamigios, Cord Jefferson and Jermaine Johnson, Producers
ANATOMY OF A FALL
Marie-Ange Luciani and David Thion, Producers
BARBIE
David Heyman, Margot Robbie, Tom Ackerley and Robbie Brenner, Producers
THE HOLDOVERS
Mark Johnson, Producer
KILLERS OF THE FLOWER MOON
Dan Friedkin, Bradley Thomas, Martin Scorsese and Daniel Lupi, Producers
MAESTRO
Bradley Cooper, Steven Spielberg, Fred Berner, Amy Durning and Kristie Macosko Krieger, Producers
OPPENHEIMER
Emma Thomas, Charles Roven and Christopher Nolan, Producers
PAST LIVES
David Hinojosa, Christine Vachon and Pamela Koffler, Producers
POOR THINGS
Ed Guiney, Andrew Lowe, Yorgos Lanthimos and Emma Stone, Producers
THE ZONE OF INTEREST
James Wilson, Producer

PRODUCTION DESIGN
BARBIE
Production Design: Sarah Greenwood; Set Decoration: Katie Spencer
KILLERS OF THE FLOWER MOON
Production Design: Jack Fisk; Set Decoration: Adam Willis
NAPOLEON
Production Design: Arthur Max; Set Decoration: Elli Griff
OPPENHEIMER
Production Design: Ruth De Jong; Set Decoration: Claire Kaufman
POOR THINGS
Production Design: James Price and Shona Heath; Set Decoration: Zsuzsa Mihalek

ANIMATED SHORT FILM
LETTER TO A PIG
Tal Kantor and Amit R. Gicelter
NINETY-FIVE SENSES
Jerusha Hess and Jared Hess
OUR UNIFORM
Yegane Moghaddam
PACHYDERME
Stéphanie Clément and Marc Rius
WAR IS OVER! INSPIRED BY THE MUSIC OF JOHN & YOKO
Dave Mullins and Brad Booker

LIVE ACTION SHORT FILM
THE AFTER
Misan Harriman and Nicky Bentham
INVINCIBLE
Vincent René-Lortie and Samuel Caron
KNIGHT OF FORTUNE
Lasse Lyskjær Noer and Christian Norlyk
RED, WHITE AND BLUE
Nazrin Choudhury and Sara McFarlane
THE WONDERFUL STORY OF HENRY SUGAR
Wes Anderson and Steven Rales

SOUND
THE CREATOR
Ian Voigt, Erik Aadahl, Ethan Van der Ryn, Tom Ozanich and Dean Zupancic
MAESTRO
Steven A. Morrow, Richard King, Jason Ruder, Tom Ozanich and Dean Zupancic
MISSION: IMPOSSIBLE - DEAD RECKONING PART ONE
Chris Munro, James H. Mather, Chris Burdon and Mark Taylor
OPPENHEIMER
Willie Burton, Richard King, Gary A. Rizzo and Kevin O'Connell
THE ZONE OF INTEREST
Tarn Willers and Johnnie Burn

VISUAL EFFECTS
THE CREATOR
Jay Cooper, Ian Comley, Andrew Roberts and Neil Corbould
GODZILLA MINUS ONE
Takashi Yamazaki, Kiyoko Shibuya, Masaki Takahashi and Tatsuji Nojima
GUARDIANS OF THE GALAXY VOL. 3
Stephane Ceretti, Alexis Wajsbrot, Guy Williams and Theo Bialek
MISSION: IMPOSSIBLE - DEAD RECKONING PART ONE
Alex Wuttke, Simone Coco, Jeff Sutherland and Neil Corbould
NAPOLEON
Charley Henley, Luc-Ewen Martin-Fenouillet, Simone Coco and Neil Corbould

WRITING (ADAPTED SCREENPLAY)
AMERICAN FICTION
Written for the screen by Cord Jefferson
BARBIE
Written by Greta Gerwig & Noah Baumbach
OPPENHEIMER
Written for the screen by Christopher Nolan
POOR THINGS
Screenplay by Tony McNamara
THE ZONE OF INTEREST
Written by Jonathan Glazer

WRITING (ORIGINAL SCREENPLAY)
ANATOMY OF A FALL
Screenplay - Justine Triet and Arthur Harari
THE HOLDOVERS
Written by David Hemingson
MAESTRO
Written by Bradley Cooper & Josh Singer
MAY DECEMBER
Screenplay by Samy Burch; Story by Samy Burch & Alex Mechanik
PAST LIVES
Written by Celine Song
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

