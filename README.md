# filmaffinityAPI
Filmaffinity API Spider developed with scrappy. Flask will be used to serve the info.

### Services:
	* Search film by name:
		As: /api/name/el%20padrino
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

