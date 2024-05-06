<?php
// Obtener el valor del parámetro 'v' de manera segura
$v = isset($_GET['v']) ? trim($_GET['v']) : '';

// Construir la URL
$filelink = 'https://streamwish.to/e/' . urlencode($v);

if (strpos($filelink, "streamwish.") !== false) {
    // User Agent
    $user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36';

    // Configuración de cURL
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $filelink);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 15);
    curl_setopt($ch, CURLOPT_TIMEOUT, 25);
    curl_setopt($ch, CURLOPT_USERAGENT, $user_agent); // Establecer el user agent
    $h = curl_exec($ch);
    curl_close($ch);

    // Extraer la URL del vídeo del contenido obtenido
    if (preg_match('/sources:\s*\[\s*{file:"([^"]+)"/', $h, $m)) {
        $link = $m[1];
    }

    // Extraer la URL de la imagen del vídeo del contenido obtenido
    if (preg_match('/image: "([^"]+)"/', $h, $img_match)) {
        $image = $img_match[1];
    }
}

// Crear el reproductor JW Player
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <script src="https://content.jwplatform.com/libraries/KB5zFt7A.js"></script>
    <script type="text/javascript">
        jwplayer.key = "XSuP4qMl+9tK17QNb+4+th2Pm9AWgMO/cYH8CI0HGGr7bdjo";
    </script>
    <div id="megaplay"></div>
    <script type="text/javascript">
        var player = jwplayer("megaplay");
        player.setup({
            "title": "PeliStart | Cine & Series",
            "description": "Mirar tu contenido de manera gratuita",
            sources: [{
                "file": "<?php echo $link; ?>",
                "type": "video/mp4",
                "label": "720p"
            }],
            width: "100vw",
            height: "100vh",
            aspectratio: "exactfit",
            startparam: "start",
            primary: "html5",
            autostart: false,
            preload: "auto",
            image: "<?php echo $image; ?>",
            advertising: {
                client: "vast",
                tag: ""
            },
            skin: {
                name: "megaplay"
            },
            captions: {
                color: "#f3f368",
                fontSize: 16,
                backgroundOpacity: 0,
                fontfamily: "Helvetica",
                edgeStyle: "raised"
            },
            tracks: [{
                file: "",
                label: "spa a2",
                kind: "captions"
            }]
        });
    </script>
    <noscript><a href="/" target="_blank"><img src="//sstatic1.histats.com/0.gif?4772667&101" alt="estadisticas web" border="0"></a></noscript>
    <!-- Histats.com  END  -->
</body>
</html>
