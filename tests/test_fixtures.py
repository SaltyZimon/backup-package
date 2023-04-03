import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def get_test_recipe_link():
    recipe_test_link = "https://shortcutapp.io/n/OGZmNTk5NTVhNDk3MWVhNDYyZTlhZGY3NTA4YjQ0YTIx"
    return recipe_test_link


@pytest.fixture
def get_test_recipe_link_corrupt():
    corrupt_recipe_test_link = "https://shortcutapp.io/n/YWI5NWY5MjhhNzUzNTIwYTExNGE5YTdkN2U4ZTBhOGJi"
    return corrupt_recipe_test_link


@pytest.fixture
def get_test_main_page():
    raw_html = """<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css\style.css">
        <script src="js\scritp.js"></script>
        <link rel="icon" href="img\icon_phone.png">
        <link rel="apple-touch-icon" sizes="76x76" href="img\icon_phone.png">
        <link rel="apple-touch-icon" sizes="120x120" href="img\icon_phone.png">
        <link rel="apple-touch-icon" sizes="152x152" href="img\icon_phone.png">
        <title>Selinas Choice</title>
    </head>

    <body>


    <!-- App -->

    <div class="app">
        <header>
            <a href="index.html">

            </a>
            <h1 class="titel">Selina's Choice</h1>

        </header>

        <div class="scroll-abstandhalter">

        </div>

        <div class="nav-feed">
            <nav>
                <button id="nav_vorspeise" class="btn"><a href="#vorspeise">Vorspeise</a></button>
                <button id="nav_hauptgang" class="btn"><a href="#hauptgang">Hauptgang</a></button>
                <button id="nav_dessert" class="btn"><a href="#dessert">Dessert</a></button>
                <button id="nav_fruehstueck" class="btn"><a href="#fruehstueck">Frühstück</a></button>
                <button id="nav_snacks" class="btn"><a href="#snacks">Snacks</a></button>
                <button id="nav_brote" class="btn"><a href="#brote">Brote</a></button>
                <button id="nav_getränke" class="btn"><a href="#getränke">Getränke</a></button>
            </nav>


            <main>
                <!-- Vorspeisen -->
                <h2 class="rezeptklassetitel" id="vorspeise">Vorspeise</h2>
                <div class="rezeptklasse">

                    <div class="rezept vorspeise">
                        <a href="https://shortcutapp.io/n/MjgzMzNlMzRkZWZmMGRiYzVjMzkxNDM2OWU0ZDA1MmQz">

                            <h3 class="rezeptname">Salvia Fritta</h3>
                        </a>
                    </div>
                    <!-- Ende Vorspeisen -->
                </div>

                <!-- Hauptgang -->
                <h2 class="rezeptklassetitel" id="hauptgang">Hauptgang</h2>
                <div class="rezeptklasse">

                    <div class="rezept hauptgang">
                        <a href="https://shortcutapp.io/n/OGZmNTk5NTVhNDk3MWVhNDYyZTlhZGY3NTA4YjQ0YTIx">
                            <img src="img\hauptgang\chilliconcarne.jpg" alt="Rezeptname">
                            <h3 class="rezeptname">Chilli Con Simon</h3>
                        </a>
                    </div>
                    <!-- Ende Hauptgang -->
                </div>

                <!-- Dessert -->
                <h2 class="rezeptklassetitel" id="dessert">Dessert</h2>
                <div class="rezeptklasse">

                    <div class="rezept dessert">
                        <a href="https://shortcutapp.io/n/YjhjMWYxODBkZTQwNTFhYWE5NWQ0YWQ1MzRkNGFiNzg5">
                            <img src="img\dessert\strudel.jpg" alt="Rezeptname">
                            <h3 class="rezeptname">Strudel dalla Nonna</h3>
                        </a>
                    </div>
                    <!-- Ende Dessert -->
                </div>


                <!-- Frühstück -->
                <h2 class="rezeptklassetitel" id="fruehstueck">Frühstück</h2>
                <div class="rezeptklasse">

                    <div class="rezept fruehstueck">
                        <a href="https://shortcutapp.io/n/ZmZjOWQ4YTczNTkwODY4MTI1ZTBiNmQ2ODNlMjYxNjEz">

                            <h3 class="rezeptname">Kokos-Porridge</h3>
                        </a>
                    </div>
                    <!-- Ende Frühstück -->
                </div>


                <!-- Snacks -->
                <h2 class="rezeptklassetitel" id="snacks">Snacks</h2>
                <div class="rezeptklasse">

                    <div class="rezept snacks">
                        <a href="https://shortcutapp.io/n/YjNhNTQxOWNjNWRkNjY3NDI0NWExYjZiODllYzRiNWVk">
                            <img src="img\snacks\knuspernuesse.jpeg" alt="Rezeptname">
                            <h3 class="rezeptname">Knuspernüsse</h3>
                        </a>
                    </div>
                    <!-- Ende Snacks -->
                </div>

                <!-- Brote -->
                <h2 class="rezeptklassetitel" id="brote">Brote</h2>
                <div class="rezeptklasse">

                    <div class="rezept brote">
                        <a href="https://shortcutapp.io/n/ZDc4MGIyOGJkMzJlY2RkY2Y1MTFjNGJjZjhkYTViZDM1">

                            <h3 class="rezeptname">Focaccia</h3>
                        </a>
                    </div>
                    <!-- Ende Brote -->
                </div>

                <!-- Getränke -->
                <h2 class="rezeptklassetitel" id="getränke">Getränke</h2>
                <div class="rezeptklasse">

                    <div class="rezept getraenke">
                        <a href="https://shortcutapp.io/n/NDczZmVmMWVmYzBhNWRjNWJkYmFiNjNiMDM2OGQ5Njg0">
                            <img src="img\getränke\Blodhound_Grapefruit.jpg" alt="Rezeptname">
                            <h3 class="rezeptname">Bloodhound Grapefruit</h3>
                        </a>
                    </div>
                    <!-- Ende Getränke -->
                </div>

                <!-- End main -->
            </main>
            <!-- End - Nav-feed -->
        </div>

        <!-- End - App -->
    </div>

    <button id="nav_author"><a style="color: black" href="https://www.linkedin.com/in/simon-ebn%C3%B6ther/">Built by Simon
        Ebnöther</a></button>

    </body>

    </html>"""
    main_page = BeautifulSoup(raw_html, 'html.parser')
    return main_page


@pytest.fixture
def get_test_recipe():
    raw_html = """<!DOCTYPE html>
    <html><head><title>Chilli Con Simon</title><meta charset="utf-8"/><meta content="IE=edge" http-equiv="X-UA-Compatible"/><meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport"/><meta content="noarchive" name="robots"/><meta content="no-preview" name="turbolinks-cache-control"/><meta content="Chilli Con Simon" name="title"/><meta name="description"/><meta content="https://files.shortcutapp.io/pzye359y_EisswKkkZYTxw/4jbBZ3_o6oxPucLcEXqmOk4cEPYAnKqM4wa2iSNzCdY?Expires=1679665497&amp;Signature=BWGGrvg5oD0KHo8J21tqzk0ggkzYgi5bikhun4dP4xmAJU91bqlWFGL8B9VPmTuhs9agouSXcjC2950qTKqMxXSk2SynpiD6YnuJsE6A6x3wbzXSVxto6glTi2pca76uolNmew9J6EX0BdtbyWlS5X8LsFFJfc7yp7lWuA9dNdNOhicn9VoU9LDpLD-hJTsBnQs5YWhf17chWi9nI~A-BQgllJpcYgxbofaQNYC~2r-tlx9uEzoXc-pda03pzFxFhqeboOG7p2jQDys90OEtpO6KA3e6DmmvtNbiEyhXgASUTGfLDEzoc76ZYOlpKD8DtIKrDJHTMUKgOGhuGs~gBw__&amp;Key-Pair-Id=APKAIJ4N3LXGOVJWMSXA" name="og:image"/><meta content="app-id=364110253, app-argument=https://shortcutapp.io/n/OGZmNTk5NTVhNDk3MWVhNDYyZTlhZGY3NTA4YjQ0YTIx" name="apple-itunes-app"/><link href="/favicons/apple-touch-icon.png?v=pglGYqJ58P" rel="apple-touch-icon" sizes="180x180"/>
    <link href="/favicons/favicon-32x32.png?v=pglGYqJ58P" rel="icon" sizes="32x32" type="image/png"/>
    <link href="/favicons/favicon-16x16.png?v=pglGYqJ58P" rel="icon" sizes="16x16" type="image/png"/>
    <link href="/favicons/site.webmanifest?v=pglGYqJ58P" rel="manifest"/>
    <link color="#ac2a1b" href="/favicons/safari-pinned-tab.svg?v=pglGYqJ58P" rel="mask-icon"/>
    <link href="/favicons/favicon.ico?v=pglGYqJ58P" rel="shortcut icon"/>
    <meta content="#ac2a1b" name="msapplication-TileColor"/>
    <meta content="/favicons/browserconfig.xml?v=pglGYqJ58P" name="msapplication-config"/>
    <meta content="#ffffff" name="theme-color"/><meta content="authenticity_token" name="csrf-param">
    <meta content="PFNPJraWM9tyCOV-9m7nwxOKYYDUn8WhjxHXGr1odvIPtWdujGUMhhKzgvY7lBMXC7C93d35Pi91rQ-Q5t0-YQ" name="csrf-token"><link href="/assets/public_content-7cb630ff9b0354328d9b1ced3ec9cfa7313d4f5842ad3c47bf4d98a9f8be3f1b.css" media="all" rel="stylesheet"/></meta></meta></head><body class="PublicContent"><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-35252564-5"></script><script>window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-35252564-5');</script><header><div class="container"><a href="/" style="line-height:0"><img src="/assets/shortcut-logo-683e1d5d192ba8781bdf32b0950b7d5f167f344a2d4c44d5ac49a37e969bda23.png"/></a><div class="stack"><a href="/"><div class="title">Shortcut — Recipes Manager</div></a><a href="#banner"><button class="download-button">Download App</button></a></div></div></header><main class="PublicNote" itemscope="" itemtype="http://schema.org/Recipe"><meta content="https://files.shortcutapp.io/pzye359y_EisswKkkZYTxw/4jbBZ3_o6oxPucLcEXqmOk4cEPYAnKqM4wa2iSNzCdY?Expires=1679665497&amp;Signature=BWGGrvg5oD0KHo8J21tqzk0ggkzYgi5bikhun4dP4xmAJU91bqlWFGL8B9VPmTuhs9agouSXcjC2950qTKqMxXSk2SynpiD6YnuJsE6A6x3wbzXSVxto6glTi2pca76uolNmew9J6EX0BdtbyWlS5X8LsFFJfc7yp7lWuA9dNdNOhicn9VoU9LDpLD-hJTsBnQs5YWhf17chWi9nI~A-BQgllJpcYgxbofaQNYC~2r-tlx9uEzoXc-pda03pzFxFhqeboOG7p2jQDys90OEtpO6KA3e6DmmvtNbiEyhXgASUTGfLDEzoc76ZYOlpKD8DtIKrDJHTMUKgOGhuGs~gBw__&amp;Key-Pair-Id=APKAIJ4N3LXGOVJWMSXA" itemprop="image"><div class="PhotoRoll" data-component="PhotoRoll"><div class="roll" data-roll=""><img alt="Chilli Con Simon" class="with-failnice" data-pop-up="true" src="https://files.shortcutapp.io/pzye359y_EisswKkkZYTxw/4jbBZ3_o6oxPucLcEXqmOk4cEPYAnKqM4wa2iSNzCdY?Expires=1679665497&amp;Signature=BWGGrvg5oD0KHo8J21tqzk0ggkzYgi5bikhun4dP4xmAJU91bqlWFGL8B9VPmTuhs9agouSXcjC2950qTKqMxXSk2SynpiD6YnuJsE6A6x3wbzXSVxto6glTi2pca76uolNmew9J6EX0BdtbyWlS5X8LsFFJfc7yp7lWuA9dNdNOhicn9VoU9LDpLD-hJTsBnQs5YWhf17chWi9nI~A-BQgllJpcYgxbofaQNYC~2r-tlx9uEzoXc-pda03pzFxFhqeboOG7p2jQDys90OEtpO6KA3e6DmmvtNbiEyhXgASUTGfLDEzoc76ZYOlpKD8DtIKrDJHTMUKgOGhuGs~gBw__&amp;Key-Pair-Id=APKAIJ4N3LXGOVJWMSXA"/></div><button class="scroll-button left" data-scroll="back"><div class="triangle"></div></button><button class="scroll-button right" data-scroll="forward"><div class="triangle"></div></button></div><section class="description"><h1 class="title" itemprop="name">Chilli Con Simon</h1><div class="by-line"><div class="timestamp"><time datetime="2021-07-09T13:04:45Z">Jul 09 2021</time></div></div><div class="description" itemprop="description"></div><div class="extra-details"><ul><li>Preparation: <time datetime="PT1H" itemprop="prepTime">about 1 hour</time></li><meta content="4" itemprop="recipeYield"/><li>Serves: 4 persons</li><li>Difficulty: medium 😀</li></ul></div></section><section class="ingredients"><h2>Ingredients</h2><ul class="IngredientList"><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Peperoni (gelb)</div></li><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Zwiebel</div></li><li itemprop="recipeIngredient"><div class="quantity">1 Zehe</div><div class="name">Knoblauch</div></li><li itemprop="recipeIngredient"><div class="quantity">4 EL</div><div class="name">Öl</div></li><li itemprop="recipeIngredient"><div class="quantity">1 EL</div><div class="name">Gemüsebujong</div></li><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Büchse Pelati (Tomaten)</div></li><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Büchse Kidneybohnen</div></li><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Büchse Mais</div></li><li itemprop="recipeIngredient"><div class="quantity">300 g</div><div class="name">Kartoffeln</div></li><li itemprop="recipeIngredient"><div class="quantity">6 EL</div><div class="name">Tomatenmark</div></li><li itemprop="recipeIngredient"><div class="quantity">500 g</div><div class="name">Rinderhackfleisch oder Quorn</div></li><li itemprop="recipeIngredient"><div class="quantity">100 ml</div><div class="name">Rotwein</div></li><li itemprop="recipeIngredient"><div class="quantity">50 ml</div><div class="name">Bier</div></li><li itemprop="recipeIngredient"><div class="quantity"></div><div class="name">Chilli je nach Schärfe</div></li><li itemprop="recipeIngredient"><div class="quantity">1 TL</div><div class="name">Basilikum und Oregano</div></li><li itemprop="recipeIngredient"><div class="quantity">2 TL</div><div class="name">Kakaopulver</div></li><li itemprop="recipeIngredient"><div class="quantity">3 TL</div><div class="name">Paprikapulver</div></li><li itemprop="recipeIngredient"><div class="quantity">1 TL</div><div class="name">Zimt</div></li><li itemprop="recipeIngredient"><div class="quantity">2 TL</div><div class="name">Kreuzkrümel (Pulver)</div></li><li itemprop="recipeIngredient"><div class="quantity">2 TL</div><div class="name">Salz</div></li><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Espresso</div></li><li itemprop="recipeIngredient"><div class="quantity">200 g</div><div class="name">Sauercreme</div></li><li itemprop="recipeIngredient"><div class="quantity">1</div><div class="name">Chiabatta Brot</div></li></ul></section><section class="instructions"><h2>Instructions</h2><ol><li><div class="details"><h3>Step 1</h3><div class="text" itemprop="recipeInstructions">Alles klein schneiden und die Zutaten bis auf die Pelati aus der Dose, in einem Sieb abwaschen.</div></div></li><li><div class="details"><h3>Step 2</h3><div class="text" itemprop="recipeInstructions">Die Zwiebeln mit Öl in der Pfanne andünsten. Danach das Fleisch oder Quorn beigeben und goldbraun anbraten. Anschliessend mit Rotwein, Bier und Espresso ablöschen.</div></div></li><li><div class="details"><h3>Step 3</h3><div class="text" itemprop="recipeInstructions">Die restlichen Zutaten und Gewürze hinzu gebeben und für 20 min mit geschlossenem Deckel köcheln lassen. Danach für 10 min unter ständigem rühren kochen, bis die gewünschte Konsistenz erreicht ist.</div></div></li><li><div class="details"><h3>Step 4</h3><div class="text" itemprop="recipeInstructions">Mit Chiabatta Brot und einem Klecks Sauercreme servieren.</div></div></li></ol></section><section class="profile"></section></meta></main><script src="/assets/public_note-c73a202325926da40a42bcffe3c833211e3217eef909981d1e083952916f1029.js"></script><footer id="banner"><div class="cta">Start collecting and managing recipes.</div><div class="badges"><a href="https://apps.apple.com/app/apple-store/id364110253"><img src="/assets/app_store_buttons/apple/en-8db899f713fdb059d268a83321cb5ccc8b8b03cf21f6e8e4fbc6e7d16e032b7d.svg"/></a></div></footer><script crossorigin="anonymous" data-cf-beacon='{"rayId":"7ace53bcbda759e9","version":"2023.3.0","r":1,"b":1,"token":"d655d26838424af1b102e78cd613354f","si":100}' defer="" integrity="sha512-M3hN/6cva/SjwrOtyXeUa5IuCT0sedyfT+jK/OV+s+D0RnzrTfwjwJHhd+wYfMm9HJSrZ1IKksOdddLuN6KOzw==" src="https://static.cloudflareinsights.com/beacon.min.js/vb26e4fa9e5134444860be286fd8771851679335129114"></script>
    </body></html>"""
    test_recipe = BeautifulSoup(raw_html, 'html.parser')
    return test_recipe
