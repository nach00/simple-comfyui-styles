# simple-comfyui-styles
Simply apply precompiled styles to ComfyUI

Credit to fretts4505 for creating the styles node
https://civitai.com/models/28238/simple-text-style-template-node-for-comfyui

Credit to ghassen2017 for compiling the list of styles
https://old.reddit.com/r/StableDiffusion/comments/15etxir/sdxl_styles/

Credit to Olivio Sarikas for workflow setup
https://www.youtube.com/watch?v=TYk6taV-gVc

I simply combined the two for use in ComfyUI. I also had to edit the `styles.csv` file to remove some incompatible characters (mostly accents). I also created the workflow based on Olivio's video, and replaced the positive and negative nodes with the new styles node. This workflow uses SDXL 1.0 Refiner for very quick image generation. 

`styles.csv` MUST go in the root folder (`ComfyUI_windows_portable`)

There is also another workflow called `3xUpscale` that you can use to increase the resolution and enhance your image. This workflow uses the upscalers: `x1_ITF_SkinDiffDetail_Lite_v1`, `4x_NMKD-Siax_200k`, `4x-UltraSharp`. I did not combine the two because the original workflow is designed for speed and simplicity. The workflow named `simple-styles-workflow-with-upscaling` will generate the image, then upscale in one process. 

Upscale models can be found here:

`x1_ITF_SkinDiffDetail_Lite_v1` https://drive.google.com/drive/folders/1VkT6tpbCPn2gKZYPtawDJGMpLg6EyRpO?usp=sharing (Source: https://upscale.wiki/wiki/Model_Database#Skin)

`4x_NMKD-Siax_200k` https://huggingface.co/gemasai/4x_NMKD-Siax_200k/tree/main

`4x-UltraSharp` https://mega.nz/folder/qZRBmaIY#nIG8KyWFcGNTuMX_XNbJ_g (Source: https://upscale.wiki/wiki/Model_Database#Universal_Models)

Alternatively, you could use StabilityAI's version, here: https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler but you'll need to clone the repo using the specified directions, as you cannot download the it normally.

Also, attached is the web extension `linkRenderNode.js` (Credit to aphaits), which enables straight lines with right angles, seen below. If you do not wish to enable this feature, you can simply delete the web/extensions folder from the repo, or change the `app.canvas.links_render_mode` variable.


0 = angular line


1 = somewhat direct, but slightly curved line


2 = normal curvy line


![image](https://github.com/nach00/simple-comfyui-styles/assets/5945533/ba38b163-ea21-4c45-8a88-8699c537f591)

![image](https://github.com/nach00/simple-comfyui-styles/assets/5945533/f2058ed7-523d-4cd5-97dc-a7b3b378ebbf)

![image](https://github.com/nach00/simple-comfyui-styles/assets/5945533/59ddc9b0-1e2c-4296-ac8c-13c0c28099c2)

![ComfyUI_00165_](https://github.com/nach00/simple-comfyui-styles/assets/5945533/c25a606f-8865-4341-bc52-394da2f92537)


Here are the list of styles available:

Manga, Oil Portrait, Sketch, 5yo drawing, Oil painting, Enhance, Anime, Photographic, Digital art, Comic book, Fantasy art, Analog film, Neonpunk, Isometric, Lowpoly, Origami, Line art, Craft clay, Cinematic, 3d-model, pixel art, Texture, Space art, Street art, Baroque, Abstract, Pointillism, Impressionist, Pop art, Minimalist, Art Deco, Cubist, Dada, Victorian, Art Nouveau, Futuristic, Medieval, Industrial, Vaporwave, Horror, Gothic, Steampunk, Retro, Surrealist, Realism, Silhouette, Collage, Watercolor, Calligraphy, Expressionist, Fauvist, Renaissance, Photorealistic, Symbolic, Avant-garde, Mosaic, Trompe l'oeil, Rococo, Macabre, Satirical, Pixelated, Futurist, Primitive, Byzantine, Psychedelic, Suprematist, Constructivist, De Stijl, Ukiyo-e, Dystopian, Biomechanical, Hyperrealism, Glitch, Trompe-l'oeil, Arabesque, Brutalist, Chiaroscuro, Tenebrism, Romantic, Bauhaus, Art brut, Metaphysical, Neoplasticism, Hard-edge, Automatism, Tachisme, Lyrical abstraction, Color field, Synthetism, Cloisonnism, Assemblage, Vorticism, Op art, Divisionism, Kinetic art, Orphism, Suprematism, Letterism, Situationalist, Sound art, Land art, Photorealistic graffiti, Hypermodern, Virtual realism, Structural film, Process art, Light and space, Post-internet, Bio-art, Byzantine, Celtic, Native American, Aboriginal, Egyptian, Mayan, Renaissance, Mughal, Romanesque, Gothic, Baroque, Rococo, Pre-Raphaelite, Impressionist, Cubist, Surrealist, Futurist, Dada, Expressionist, Fauvist, Socialist Realist, Pop Art, Suprematism, Symbolist, Pre-Columbian, Constructivist, Art Nouveau, Precisionist, Neoclassical, Persian Miniature, Edo, Tribal, Tibetan Thangka, Art Deco, Minimalist, Greek Classical, African, Russian Iconography, Nordic, Inuit, Maori, Iznik, Ottoman, Hanami, Mandala, Aztec, Sumi-e, Ukiyo-e, Haida, Moorish, Victorian, Pueblo, Cloisonne, Khokhloma, Biedermeier, Goryeo, Han, Hellenistic, Tang, Ming, Joseon, Gupta, Pallava, Chola, Minoan, Mycenaean, Ndebele, San, Batik, Assyrian, Thracian, Etruscan, Sumerian, Babylonian, Norse, Olmec, Toltec, Sican, Nazca, Inca, Zapotec, Mixtec, Ottonian, Merovingian, Carolingian, Otomi, Huichol, Ainu, Maori, Aboriginal, Inuit, Saami, Ojibwe, Tlingit, Navajo, Apache, Zuni, Hopi, Sioux, Lakota, Yupik, Cherokee, Mohawk, Cree, Acoma, Laguna, Seminole, Osage, Anasazi, Mimbres, Pomo, Hohokam, Mississippian, Fremont, Mogollon, Salado, Zulu, Maasai, Ndebele, Kuba, Yoruba, Akan, Berber, Dogon, Fang, Baga, Blade Runner, Star Wars, Lord of the Rings, Matrix, Indiana Jones, Mad Max, 2001: A Space Odyssey, Alien, Avatar, Pulp Fiction, Kill Bill, Inception, Fight Club, Harry Potter, Marvel Cinematic Universe, DC Extended Universe, Game of Thrones, Twilight, Transformers, The Hunger Games, Pirates of the Caribbean, Jurassic Park, The Shining, The Godfather, The Dark Knight, Casablanca, Jaws, The Wizard of Oz, E, Ghostbusters, Back to the Future, Toy Story, The Lion King, Finding Nemo, Shrek, The Little Mermaid, Aladdin, Beauty and the Beast, Cinderella, Sleeping Beauty, Snow White, Mulan, Pocahontas, The Nightmare Before Christmas, Frozen, Moana, Tangled, Zootopia, Coco, Brave, Inside Out, The Incredibles, Up, Wall-E, Ratatouille, Monsters Inc, Cars, A Bug's Life, James Bond, Fast and Furious, Mission Impossible, Jurassic World, Minions, Interstellar, The Grinch, Avengers: Endgame, Wonder Woman, The Iron Giant, Godzilla, King Kong, The Grand Budapest Hotel, Inside Llewyn Davis, Drive, The Neon Demon, It Follows, Dunkirk, Her, The Revenant, Whiplash, The Shape of Water, A Ghost Story, The Florida Project, La La Land, The Lobster, Ex Machina, Birdman, Gravity, The Tree of Life, Inception, The Social Network, Moonlight, Roma, Parasite, 1917, Jojo Rabbit, Joker, The Lighthouse, Once Upon a Time in Hollywood, The Irishman, Uncut Gems, Little Women, Knives Out, Marriage Story, Midsommar, Booksmart, Ford v Ferrari, Rocketman, Ad Astra, Waves, The Farewell, Hustlers, Portrait of a Lady on Fire, Pain and Glory, The Two Popes, A Beautiful Day in the Neighborhood, The Peanut Butter Falcon, The Goldfinch, High Life, The Nightingale, Yesterday, Doctor Sleep, The Farewell, John Wick 3, Us, The Irishman, Honey Boy, Joker, Uncut Gems, 1917, Ford v Ferrari, Cats, Jojo Rabbit, Parasite, The Lion King, Aladdin, Toy Story 4, Avengers: Endgame, Star Wars: The Rise of Skywalker, Downton Abbey, Frozen 2, Little Women, 2D Traditional Animation, CGI Animation, Stop-Motion Animation, Claymation, Vector Animation, Flash Animation, Rotoscope Animation, Cut-Out Animation, Sand Animation, Pixel Art Animation, Anime Style Animation, Manga Style Art, Chibi Style Art, Superflat, Ukiyo-e, Western Comics Art, Graphic Novel Art, Cartoon Modern, Abstract Animation, Silhouette Animation, Looney Tunes, Disney Classic, Studio Ghibli, Pixar, Shonen, Mecha, Shojo, Nickelodeon, Cartoon Network, Adult Swim, Adventure Time, Rick and Morty, South Park, The Simpsons, Family Guy, Bob's Burgers, Gravity Falls, Steven Universe, One Piece, Attack on Titan, My Hero Academia, Naruto, Dragon Ball Z, Sailor Moon, Cowboy Bebop, Van Gogh, Warhol, Picasso, Da Vinci, Monet, Dali, Pollock, Rothko, Matisse, Banksy, Michelangelo, Kusama, Hokusai, O'Keeffe, Cezanne, Hopper, Klimt, Chagall, Lichtenstein, Basquiat, Frida Kahlo, Georgia O'Keeffe, Jackson Pollock, Rembrandt, Renoir, Magritte, Manet, Vermeer, Caravaggio, Rodin, Botticelli, Edward Hopper, Keith Haring, Damien Hirst, Yayoi Kusama, Francis Bacon, Ai Weiwei, Cindy Sherman, Frank Stella, Lucian Freud, Marc Chagall, Roy Lichtenstein, Thomas Kinkade, Joan Miró, Gerhard Richter, Wassily Kandinsky, Norman Rockwell, Bridget Riley, Piet Mondrian, Salvador Dali, Mary Cassatt, Diego Rivera, Jean-Michel Basquiat, Henry Moore, Frida Kahlo, Grant Wood, Edward Hopper, Andy Goldsworthy, Louise Bourgeois, Ansel Adams, Yoko Ono, Gustav Klimt, Jeff Koons, John Singer Sargent, Marcel Duchamp, Claude Monet, Anish Kapoor, Hieronymus Bosch, Paul Gauguin, Katsushika Hokusai, Pierre-Auguste Renoir, Antony Gormley, Kazimir Malevich, Jean-Antoine Watteau, Constantin Brancusi, Egon Schiele, Nam June Paik, James Whistler, Wassily Kandinsky, Lucio Fontana, Artemisia Gentileschi, Jean Dubuffet, Sandro Botticelli, Carl Andre, David Hockney, Cindy Sherman, Jenny Holzer, Dante Gabriel Rossetti, Zaha Hadid, Takashi Murakami, Edward Weston, Edvard Munch, Ai Weiwei, Georges Braque, Sol LeWitt, Mary Cassatt, Damien Hirst, Giuseppe Arcimboldo, Yves Klein, Frida Kahlo, Piet Mondrian, Bridget Riley, Mark Rothko, Joseph Beuys, Berthe Morisot, Agnes Martin, Yayoi Kusama, Andy Goldsworthy, Henri Cartier-Bresson, Marina Abramovic, Man Ray, Kathe Kollwitz, Robert Rauschenberg, Lyonel Feininger, Tracey Emin, Rene Magritte, Henry Moore, Rachel Whiteread, Tomma Abts, Max Ernst, Richard Serra, Ernst Ludwig Kirchner, Eva Hesse, Paul Cezanne, Francis Bacon, Louise Bourgeois, Chuck Close, Thomas Gainsborough, Gerhard Richter, Jean-Michel Basquiat, Alexander Calder, Jackson Pollock, Anselm Kiefer, Amedeo Modigliani, Gilbert & George, El Greco, Salvador Dali, Rembrandt van Rijn, Keith Haring, Georgia O'Keeffe, Caravaggio, Louise Nevelson, James Turrell, edouard Manet, Marc Chagall, Dan Flavin, Sarah Lucas, Johannes Vermeer, Tadao Ando, Roy Lichtenstein, Joseph Cornell, Gustave Courbet, Richard Long, Otto Dix, Barnett Newman, Sophie Calle, KAWS, Francis Picabia, H, Jean Arp, Ai Weiwei, Fernand Leger, Yoko Ono, Cindy Sherman, Nam June Paik, Barbara Kruger, Piero della Francesca, Georgia O'Keeffe, Richard Hamilton, Kazimir Malevich, Grayson Perry, Faith Ringgold, Banksy, Tracey Emin, Olafur Eliasson, Kiki Smith, David Hockney, Chris Ofili, Ellsworth Kelly, Christo and Jeanne-Claude, Wayne Thiebaud, Jenny Holzer, Antony Gormley, Maurice Sendak, Charismatic, Cinematic, Environmental, Reportage, Candid, Documentary, Haute Couture, Editorial, Catalog, Action-packed, Emotional, Narrative, Minimalistic, Dramatic, Rustic, Investigative, Lifestyle, Opinion, Historical, Modernist, Surreal, Steampunk, Futuristic, Abstract Expressionism, Surrealism, Watercolor, Pointillism, Cubism, Gothic, Pop Art, Impressionism, Street Art, Art Nouveau, Charcoal, Collage, Minimalist, Graffiti, Trompe L'oeil, Fauvism, Hyperrealism, Dada, Calligraphy, Baroque, Op Art, Psychedelic, Scratchboard, Botanical Illustration, Lithography, Mosaic, Woodcut, Stencil Art, Rotoscoping, Glass Painting, Art Deco, Hard Edge Painting, Drybrush, Silhouette, Plein Air, Ink Wash, Body Painting, Spray Paint, Grisaille, Stippling, Pastel, Encaustic, Macrame, Graffiti Stencil, Action Painting, Batik, Folk Art, Glitch Art, Chiaroscuro, Gouache, High-Fashion, Casual-Chic, Streetwear, Athletic, Vintage, Bohemian, Minimalist, Preppy, Gothic, Punk, Grunge, Glamorous, Rocker, Hipster, Ethical, Business Casual, Beachwear, Activewear, Country, Military, Kawaii, Lolita, Formal, Tomboy, Normcore, Artistic, Genderless, Monochromatic, Mod, Harajuku, Cyberpunk, Rave, Hippy, Skater, Pin-Up, Nautical, Futuristic, Eccentric, Tailored, Sustainable, Traditional, Candid, Portrait, Lifestyle, Editorial, Glamour, Fitness, Boudoir, Silhouette, Maternity, Black and White, Pin-Up, Headshot, Full Body, High Fashion, Business, Beach, Lingerie, Athletic, Close-up, Nature, Studio, Street, Dance, Vintage, Low Light, Underwater, Action, Fashion, Aerial, Music, Abstract, Fine Art, Cityscape, Landscape, Macro, Golden Hour, Blue Hour, Night, Reflection, Backlit, Overhead
