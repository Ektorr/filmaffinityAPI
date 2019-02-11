# filmaffinityAPI
Filmaffinity API Spider developed with scrappy. Flask will be used to serve the info.

### Services:
* Search film by name:
	As: /api/name/el%20padrino
* Search film by ID:
	/api/636548/ 
* Get a list with all the topics:
	/api/topics
* Get a list with all the films IDS of a determinated topic:
	/api/films_by_topic/<id_topic>/<limit>/ -> /api/topic/461156/2/ (Only will return 2 films of topic 461156)

	limit = 0, all the films of a selected topic

Both will return a JSON with the data film.

	```
	{
	  "content": [
	    {
	      "actors": [
		{
		  "name": "Nelly Karim", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Nelly%20Karim"
		}, 
		{
		  "name": "Hany Adel", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Hany%20Adel"
		}, 
		{
		  "name": "El Sebaii Mohamed", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=El%20Sebaii%20Mohamed"
		}, 
		{
		  "name": "Ahmed Abdelhamid Hefny", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Ahmed%20Abdelhamid%20Hefny"
		}, 
		{
		  "name": "Mahmoud Fares", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Mahmoud%20Fares"
		}, 
		{
		  "name": "Waleed Abdel Ghany", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Waleed%20Abdel%20Ghany"
		}, 
		{
		  "name": "Ahmed Dash", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=cast&sn&stext=Ahmed%20Dash"
		}
	      ], 
	      "awards": [
		{
		  "name": "Festival de Cannes: Seccion \"Un Certain Regard\"", 
		  "url": "https://www.filmaffinity.com/es/awards.php?award_id=cannes&year=2016", 
		  "year": "2016"
		}, 
		{
		  "name": "Festival de Valladolid - Seminci: Mejor nuevo director y Mejor fotografia", 
		  "url": "https://www.filmaffinity.com/es/awards.php?award_id=seminci&year=2016", 
		  "year": "2016"
		}
	      ], 
	      "country": "Egipto", 
	      "critics": [
		{
		  "author": "Jay Weissberg", 
		  "country": "Estados Unidos", 
		  "gender": "M", 
		  "media": "Variety", 
		  "status": "POS", 
		  "text": "Presentando un trabajo de camara excelente del director de fotografia Ahmed Gabr y una direccion estelar de la multitud, 'Clash' puede sorprender a algunos por recaer demasiado en la histeria, aun asi es cine brillante ", 
		  "url": "http://variety.com/2016/film/festivals/cannes-film-review-clash-1201773347/"
		}, 
		{
		  "author": "Deborah Young", 
		  "country": "Estados Unidos", 
		  "gender": "F", 
		  "media": "The Hollywood Reporter", 
		  "status": "POS", 
		  "text": "Poderosa y muy perturbadora (...) Sorprendentemente, la pelicula no se posiciona a favor de ningun lado. ", 
		  "url": "http://www.hollywoodreporter.com/review/clash-eshtebak-cannes-review-893496"
		}, 
		{
		  "author": "Jaime N. Christley", 
		  "country": "Estados Unidos", 
		  "gender": "M", 
		  "media": "Slant", 
		  "status": "POS", 
		  "text": "'Clash' funciona bien basandose en una premisa excelente ", 
		  "url": "http://www.slantmagazine.com/house/article/cairo-international-film-festival-the-other-land-we-are-never-alone-clash-home-sweet-home-kills-on-wheels-mimosas-and-more"
		}, 
		{
		  "author": "Benjamin Lee", 
		  "country": "Reino Unido", 
		  "gender": "M", 
		  "media": "The Guardian", 
		  "status": "POS", 
		  "text": "[Un] thriller perturbador y tecnicamente audaz (...) Aunque solo es la segunda pelicula de Diab (...) su destreza es impresionante (...) Puntuacion:  (sobre 5) ", 
		  "url": "https://www.theguardian.com/film/2016/may/13/clash-review-egyptian-revolution"
		}, 
		{
		  "author": "Lee Marshall", 
		  "country": "Reino Unido", 
		  "gender": "M", 
		  "media": "Screendaily", 
		  "status": "POS", 
		  "text": "'Clash' es intensamente cinematografica, usa la camara en mano en un espacio reducido de forma original como espejo de una sociedad sin espacio para maniobrar. ", 
		  "url": "http://www.screendaily.com/reviews/clash-cannes-review/5103774.article"
		}, 
		{
		  "author": "David Stratton", 
		  "country": "Australia", 
		  "gender": "M", 
		  "media": "The Australian", 
		  "status": "POS", 
		  "text": "Una experiencia visual fascinante (...) Es una idea atrevida y funciona muy bien ", 
		  "url": "http://www.theaustralian.com.au/arts/review/film-reviews-life-with-jake-gyllenhaal-clash-zachs-ceremony/news-story/15b3920f9ae8490ff7e19a8eb6bc9279"
		}, 
		{
		  "author": "Javier Ocana", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Diario El Pais", 
		  "status": "POS", 
		  "text": "Con un magnifico uso del sonido, el montaje y los colores (...) Diab articula una obra mas fisica que analitica, en la que siempre ganan las sensaciones en detrimento del examen dramatico. ", 
		  "url": "http://cultura.elpais.com/cultura/2017/06/01/actualidad/1496292463_823539.html"
		}, 
		{
		  "author": "Luis Martinez", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Diario El Mundo", 
		  "status": "POS", 
		  "text": "<<Una esfera infinita, cuyo centro esta en todas partes y la circunferencia en ninguna>>. Asi definia Pascal el universo y asi construye el egipcio Mohamed Diab su admirable Clash  (...) Puntuacion:  (sobre 5) ", 
		  "url": "http://www.elmundo.es/metropoli/cine/2017/06/01/592ed8a9268e3e0b248b471e.html"
		}, 
		{
		  "author": "Oti Rodriguez Marchante", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Diario ABC", 
		  "status": "POS", 
		  "text": "La fuerte sensacion de aturdimiento en el espectador, incapaz de entender y personalizar el caos (...), no es mas que un reflejo de la mirada de Occidente a ese lugar lejanisimo. (...) Puntuacion:  (sobre 5) ", 
		  "url": "http://www.abc.es/play/cine/criticas/abci-clash-avispero-primavera-arabe-201706011938_noticia.html"
		}, 
		{
		  "author": "Nando Salva", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Diario El Periodico", 
		  "status": "POS", 
		  "text": "La estrategia narrativa sirve para crear una atmosfera irrespirable de tension claustrofobica (...) el escenario funciona como metaforico lamento  (...) Puntuacion:  (sobre 5) ", 
		  "url": "http://www.elperiodico.com/es/noticias/ocio-y-cultura/critica-pelicula-clash-mohamed-diab-6074942"
		}, 
		{
		  "author": "Sergi Sanchez", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Diario La Razon", 
		  "status": "POS", 
		  "text": "Mohammed Diab reivindica la via de la reconciliacion para contar, con animo didactico, una realidad de una complejidad que, en Occidente, sigue siendonos desconocida. ", 
		  "url": "http://www.larazon.es/cultura/cine/george-clooney-america-no-se-mueve-por-el-miedo-BE12618900?sky=Sky-Mayo-2016#Ttt1sf6uF4Z78uJt"
		}, 
		{
		  "author": "Carlos Maranon", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Cinemania", 
		  "status": "POS", 
		  "text": "Diab encierra en un solo espacio escenico a un abanico de personajes (...) que le sirve para desarrollar un choque dialectico tan eficaz como tramposo (...) logra elevar el deja vu a un estadio supremo (...) Puntuacion:  (sobre 5) ", 
		  "url": "http://cinemania.elmundo.es/peliculas/clash/critica/"
		}, 
		{
		  "author": "Jordi Batlle Caminal", 
		  "country": "Espana", 
		  "gender": "M", 
		  "media": "Fotogramas", 
		  "status": "NEU", 
		  "text": "No tarda en encallarse: (...) donde se cuece la historia no manifiesta excesivo progreso ni los personajes (cliches la mayoria) tienen suficiente entidad para elevar el interes del asfixiante relato (...) Puntuacion:  (sobre 5) ", 
		  "url": "http://www.fotogramas.es/Peliculas/Clash#critFG"
		}, 
		{
		  "author": "Pablo O. Scholz", 
		  "country": "Argentina", 
		  "gender": "M", 
		  "media": "Diario Clarin", 
		  "status": "POS", 
		  "text": "Filme de tinte politico pero con su costado social, (...) las disputas y la claustrofobia llegan a incomodar verdaderamente al espectador. ", 
		  "url": "http://www.clarin.com/extrashow/cine/George-Clooney-maestro-seduccion_0_1575442511.html"
		}, 
		{
		  "author": "Samuel Castro", 
		  "country": "Colombia", 
		  "gender": "M", 
		  "media": "Diario El Colombiano", 
		  "status": "POS", 
		  "text": "No solo es una gran historia y un fascinante ejercicio de estilo, es una poderosa manera de acercarnos a una sociedad tan compleja como la egipcia y tratar de entender sus acontecimientos politicos recientes. ", 
		  "url": "http://www.elcolombiano.com/opinion/criticos/un-mundo-contenido-JB7047920"
		}, 
		{
		  "author": "Manuel Kalmanovitz G.", 
		  "country": "Colombia", 
		  "gender": "M", 
		  "media": "Revista Semana", 
		  "status": "POS", 
		  "text": "Lo mas impresionante de este filme ingenioso, tensionante y de bajo presupuesto es la dinamica de la destruccion: cuando comienza y coge impulso arrasa con todo lo que se le atraviese. (...) Puntuacion:  (sobre 4) ", 
		  "url": "http://www.semana.com/cultura/articulo/clash-critica-por-kalmanovitz/534814"
		}, 
		{
		  "author": "Gustavo Valencia Patino", 
		  "country": "Colombia", 
		  "gender": "M", 
		  "media": "Revista Semana", 
		  "status": "POS", 
		  "text": "La pelicula se convierte en una radiografia muy exacta de toda una idiosincrasia y sus patrones de comportamiento. Un particular dibujo no solo del agitado momento socio-politico de esa nacion, sino antes que nada un intento de retratar al ser humano cuando se refiere a la defensa de sus ideas, ", 
		  "url": "http://www.semana.com/cultura/articulo/clash-de-mohamed-diab/537952"
		}, 
		{
		  "author": "Martha Ligia Parra", 
		  "country": "Colombia", 
		  "gender": "F", 
		  "media": "Diario El Tiempo", 
		  "status": "POS", 
		  "text": "La pelicula es un relato intenso y vibrante captado como si se tratara de hechos reales que se registran en caliente. ", 
		  "url": "http://www.eltiempo.com/colombia/medellin/clash-todos-en-el-mismo-barco-116176"
		}
	      ], 
	      "directors": [
		{
		  "name": "Mohamed Diab", 
		  "url": "https://www.filmaffinity.com/es/search.php?stype=director&sn&stext=Mohamed%20Diab"
		}
	      ], 
	      "duration": "97 min.", 
	      "genres": [
		{
		  "name": "Drama", 
		  "url": "https://www.filmaffinity.com/es/moviegenre.php?genre=DR&attr=rat_count&nodoc"
		}
	      ], 
	      "guionists": [
		"Khaled Diab", 
		"Mohamed Diab"
	      ], 
	      "id": 836362, 
	      "images": {
		"bluray": [], 
		"bso": [], 
		"dvd": [], 
		"events": [], 
		"frames": [
		  "https://pics.filmaffinity.com/Clash-391572346-large.jpg"
		], 
		"making_of": [], 
		"others": [], 
		"posters": [
		  "https://pics.filmaffinity.com/Clash-107889267-large.jpg", 
		  "https://pics.filmaffinity.com/Clash-417377895-large.jpg", 
		  "https://pics.filmaffinity.com/Clash-494263211-large.jpg", 
		  "https://pics.filmaffinity.com/Clash-911363744-large.jpg"
		], 
		"promo": [], 
		"vhs": [], 
		"wallpapers": []
	      }, 
	      "musicians": [
		"Khaled Dagher"
	      ], 
	      "name": "Eshtebak", 
	      "photography": [
		"Ahmed Gabr"
	      ], 
	      "producer": [
		"Sampek Productions"
	      ], 
	      "rating": {
		"critics": 657, 
		"note": 6.9
	      }, 
	      "spanish_name": "Clash", 
	      "summary": "El Cairo, verano de 2013, dos anos despues de la revolucion egipcia. Tras la destitucion del presidente islamista Morsi, en un dia de violentos disturbios, la  policia detiene y encierra en un furgon a decenas de manifestantes con convicciones politicas y religiosas diferentes.", 
	      "trailers": [
		"https://www.dailymotion.com/embed/video/x5new45?queue-enable=false&autoplay=false"
	      ], 
	      "url": "https://www.filmaffinity.com/es/film836362.html", 
	      "year": "2016"
	    }
	  ], 
	  "status": true
	}
	```

