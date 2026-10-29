"""Testes do conversor deck/ -> site/index.html (só o que não é cópia literal)."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("build_site", ROOT / "tools" / "build-site.py")
bs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bs)

TAG = (
    '<x-capture src="img/portfolio.png" alt="Portfólio" '
    'style="width:880px;height:458px"></x-capture>'
)
IMG = '<img src="img/portfolio.png" alt="Portfólio" style="width:880px;height:458px">'


class CaptureTest(unittest.TestCase):
    """O elemento x-capture vira <img> ou bloco reservado conforme o arquivo exista."""

    def setUp(self):
        """Cria um site/ temporário com img/ vazio."""
        self._tmp = tempfile.TemporaryDirectory()
        self.site_dir = Path(self._tmp.name)
        (self.site_dir / "img").mkdir()

    def tearDown(self):
        """Remove o site/ temporário."""
        self._tmp.cleanup()

    def test_capture_sem_arquivo_vira_bloco_reservado(self):
        """Sem o arquivo, o slide mostra 'captura: <nome>' no lugar da imagem."""
        out = bs.capture(TAG, self.site_dir)
        self.assertIn('class="captura"', out)
        self.assertIn("captura: portfolio.png", out)
        self.assertIn("width:880px;height:458px", out)
        self.assertNotIn("<img", out)

    def test_capture_com_arquivo_vira_img(self):
        """Com o arquivo em site/img/, o slide mostra a imagem sem edição."""
        (self.site_dir / "img" / "portfolio.png").write_bytes(b"\x89PNG")
        self.assertEqual(bs.capture(TAG, self.site_dir), IMG)

    def test_convert_troca_x_capture(self):
        """convert() aplica a troca dentro de um slide inteiro."""
        html = '<section id="s" style="">' + TAG + "</section>"
        self.assertIn("captura: portfolio.png", bs.convert(html, self.site_dir))


if __name__ == "__main__":
    unittest.main()
