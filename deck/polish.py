"""Post-process the built deck: larger table text, content-based column widths, no auto chart titles."""
import sys
from pptx import Presentation
from pptx.util import Pt, Emu


def text_width(s):
    # CJK characters are roughly twice as wide as Latin ones
    return sum(2 if ord(c) > 0x2E80 else 1 for c in s)


def polish(path):
    prs = Presentation(path)
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_chart:
                shape.chart.has_title = False
            if not shape.has_table:
                continue
            tbl = shape.table
            ncols = len(tbl.columns)
            weights = [max(text_width(tbl.cell(r, c).text) for r in range(len(tbl.rows))) + 4
                       for c in range(ncols)]
            total = shape.width
            for c, w in enumerate(weights):
                tbl.columns[c].width = Emu(int(total * w / sum(weights)))
            body_pt = 14 if ncols > 2 else 15
            for r, row in enumerate(tbl.rows):
                row.height = Pt(34)
                for cell in row.cells:
                    cell.vertical_anchor = 3  # middle
                    for p in cell.text_frame.paragraphs:
                        for run in p.runs:
                            run.font.size = Pt(body_pt)
    prs.save(path)


if __name__ == "__main__":
    polish(sys.argv[1])
    print("polished", sys.argv[1])
