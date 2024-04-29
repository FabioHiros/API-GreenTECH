function mudarImagem(caminho) {
    document.getElementById('imagem').src = caminho;
    // Mostra a tabela correspondente e oculta as outras
    if (caminho.includes('grafico_Index.jpg')) {
        document.getElementById('tabela-media').style.display = 'block';
        document.getElementById('tabela-temperatura').style.display = 'none';
        document.getElementById('tabela-umidade-amb').style.display = 'none';
        document.getElementById('tabela-umidade-solo').style.display = 'none';
    } else if (caminho.includes('temperatura.jpeg')) {
        document.getElementById('tabela-media').style.display = 'none';
        document.getElementById('tabela-temperatura').style.display = 'block';
        document.getElementById('tabela-umidade-amb').style.display = 'none';
        document.getElementById('tabela-umidade-solo').style.display = 'none';
    } else if (caminho.includes('umidade_amb.jpeg')) {
        document.getElementById('tabela-media').style.display = 'none';
        document.getElementById('tabela-temperatura').style.display = 'none';
        document.getElementById('tabela-umidade-amb').style.display = 'block';
        document.getElementById('tabela-umidade-solo').style.display = 'none';
    } else if (caminho.includes('umidade_solo.jpeg')) {
        document.getElementById('tabela-media').style.display = 'none';
        document.getElementById('tabela-temperatura').style.display = 'none';
        document.getElementById('tabela-umidade-amb').style.display = 'none';
        document.getElementById('tabela-umidade-solo').style.display = 'block';
    }
}