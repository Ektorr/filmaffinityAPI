# filmaffinityAPI
Filmaffinity API Spider developed with scrappy. Flask will be used to serve the info.

###Services:
	* Search film by name:
		As: /api/by_name/el%20padrino
	* Search film by ID:
		/api/636548/ 

	Both will return a JSON with the data film.

	```
	{
	  "content": [
	    {
	      "actors": [
	        {
	          "name": "Jose Isbert", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Isbert"
	        }, 
	        {
	          "name": "Nino Manfredi", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Nino%20Manfredi"
	        }, 
	        {
	          "name": "Emma Penella", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Emma%20Penella"
	        }, 
	        {
	          "name": "Jose Luis Lopez Vazquez", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Luis%20L%C3%B3pez%20V%C3%A1zquez"
	        }, 
	        {
	          "name": "Angel Alvarez", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=%C3%81ngel%20%C3%81lvarez"
	        }, 
	        {
	          "name": "Maria Luisa Ponte", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Mar%C3%ADa%20Luisa%20Ponte"
	        }, 
	        {
	          "name": "Maria Isbert", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Mar%C3%ADa%20Isbert"
	        }, 
	        {
	          "name": "Julia Caba Alba", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Julia%20Caba%20Alba"
	        }, 
	        {
	          "name": "Guido Alberti", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Guido%20Alberti"
	        }, 
	        {
	          "name": "Erasmo Pascual", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Erasmo%20Pascual"
	        }, 
	        {
	          "name": "Xan das Bolas", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Xan%20das%20Bolas"
	        }, 
	        {
	          "name": "Jose Orjas", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Orjas"
	        }, 
	        {
	          "name": "Jose Maria Prada", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Mar%C3%ADa%20Prada"
	        }, 
	        {
	          "name": "Felix Fernandez", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=F%C3%A9lix%20Fern%C3%A1ndez"
	        }, 
	        {
	          "name": "Antonio Ferrandis", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Antonio%20Ferrandis"
	        }, 
	        {
	          "name": "Lola Gaos", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Lola%20Gaos"
	        }, 
	        {
	          "name": "Alfredo Landa", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Alfredo%20Landa"
	        }, 
	        {
	          "name": "Jose Sazatornil", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Sazatornil"
	        }, 
	        {
	          "name": "Agustin Gonzalez", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Agust%C3%ADn%20Gonz%C3%A1lez"
	        }, 
	        {
	          "name": "Chus Lampreave", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Chus%20Lampreave"
	        }, 
	        {
	          "name": "Jose Luis Coll", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Luis%20Coll"
	        }, 
	        {
	          "name": "Jose Cordero", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Jos%C3%A9%20Cordero"
	        }, 
	        {
	          "name": "Pedro Beltran", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Pedro%20Beltr%C3%A1n"
	        }, 
	        {
	          "name": "Dolores Garcia", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Dolores%20Garc%C3%ADa"
	        }, 
	        {
	          "name": "Emilio Laguna", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Emilio%20Laguna"
	        }, 
	        {
	          "name": "Enrique Tusquets", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Enrique%20Tusquets"
	        }, 
	        {
	          "name": "Enrique Pelayo", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Enrique%20Pelayo"
	        }
	      ], 
	      "awards": [
	        {
	          "name": "Festival de Venecia: Premios FIPRESCI", 
	          "url": "https://www.filmaffinity.com/es/awards.php?award_id=venice&year=1963", 
	          "year": "1963"
	        }
	      ], 
	      "country": "Espa\u00f1a", 
	      "directors": [
	        {
	          "name": "Luis Garcia Berlanga", 
	          "url": "https://www.filmaffinity.com/es/search.php?stype=director&sn&stext=Luis%20Garc%C3%ADa%20Berlanga"
	        }
	      ], 
	      "duration": "90 min.", 
	      "genres": [
	        {
	          "name": "Comedia", 
	          "url": "https://www.filmaffinity.com/es/moviegenre.php?genre=CO&attr=rat_count&nodoc"
	        }
	      ], 
	      "guionists": [
	        "Rafael Azcona", 
	        "Luis Garc\u00eda Berlanga", 
	        "Ennio Flaiano"
	      ], 
	      "images": {
	        "large": "https://pics.filmaffinity.com/el_verdugo-396316416-large.jpg", 
	        "medium": "https://pics.filmaffinity.com/el_verdugo-396316416-mmed.jpg", 
	        "small": "https://pics.filmaffinity.com/el_verdugo-396316416-small.jpg"
	      }, 
	      "musicians": [
	        "Miguel Asins Arb\u00f3"
	      ], 
	      "name": "El verdugo", 
	      "photography": [
	        "Tonino Delli Colli (B&W)"
	      ], 
	      "producer": [
	        "Coproduccion Espana-Italia; Naga Films", 
	        "Zabra Films"
	      ], 
	      "rating": {
	        "critics": 36554, 
	        "note": 8.3
	      }, 
	      "summary": "Jose Luis, el empleado de una funeraria, proyecta emigrar a Alemania para convertirse en un buen mecanico. Su novia es hija de Amadeo, un verdugo profesional. Cuando este los sorprende en la intimidad, los obliga a casarse. Ante la acuciante falta de medios economicos de los recien casados, Amadeo, que esta a punto de jubilarse, trata de persuadir a Jose Luis para que solicite la plaza que el va a dejar vacante, lo que le daria derecho a una vivienda. Jose Luis acaba aceptando la propuesta de su suegro con el convencimiento de que jamas se presentara la ocasion de ejercer tan ignominioso oficio.", 
	      "url": "https://www.filmaffinity.com/es/film411856.html", 
	      "year": "1963"
	    }
	  ], 
	  "status": true
	}
	```

