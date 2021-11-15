import json
import fitz
from fitz.fitz import STAMP_Experimental
import io
import pdfCropMargins
import pdf2image


class InvalidChapter(Exception):
    pass
class InvalidExercise(Exception):
    pass
class InternalError(Exception):
    pass


def create_image(ch, ex):
    """
    Takes a chapter and exercise number and return a PIL image of the exercise
    """
    def find_ex_rect(ex_num):
        matches = page.search_for(f"{ex_num}. ")
        rects = []
        for n in range(len(matches)):
            if matches[n].x0 < 100:
                rects.append(matches[n])

        if len(rects) > 1:
            print(f"Error: Too many matchs for exercise {ex_num} on page {pg_num} in chap {ch_num}")
            raise
        elif len(rects) < 1:
            print(f"Error: No match for exercise {ex_num} on page {pg_num} in chap {ch_num}")
            raise
            
        return rects[0]


    ch_num = str(ch)
    ex_num = str(ex)

    with open("dadanswers/index.json") as f:
        index = json.load(f)

    if not ch_num in index:
        print(f"Chapter {ch_num} doesn't exist")
        raise InvalidChapter
    elif not ex_num in index[ch_num]:
        print(f"Exercises {ex_num} doesn't exist in chapter {ch_num}")
        raise InvalidExercise
    pg_num = index[ch_num][ex_num]

    pdf = fitz.open(f"dadanswers/chapters/chap{ch_num}.pdf")
    output = fitz.open()

    x, y, width, height = pdf.load_page(pg_num).rect

    # Margins:
    # +-----+
    # |+---+|--> 35
    # ||   ||
    # |+---+|--> 115
    # +-----+

    crop = fitz.Rect(0, 35, width, height - 115)
    page = output.new_page(-1, crop.width, crop.height*3)
    for i in range(min(3, pdf.page_count - pg_num)):
        page.show_pdf_page(crop + (0, crop.height * i, 0, crop.height * i), pdf, pg_num + i, clip = crop)
    pdf.close()

    page = output.load_page(0)

    try:
        ex_rect = find_ex_rect(ex_num)
        next_ex_rect = find_ex_rect(str(int(ex_num) + 1))
    except:
        raise InternalError

    highlight_rect = page.search_for(f"{ex_num}.", clip = ex_rect)[0]
    highlight = page.add_highlight_annot(highlight_rect)
    highlight.set_colors(stroke=(1.0, 0.5, 0.0))
    highlight.update()

    top = ex_rect.y0 - 8
    bottom = next_ex_rect.y0 - 8
    width = page.cropbox.width
    page.set_cropbox(fitz.Rect(0, top, width, bottom))

    # stamp = page.add_stamp_annot(page.cropbox, STAMP_Experimental)
    # stamp.set_opacity(0.05)
    # stamp.update()

    output.save("dadanswers/temp/temp.pdf", deflate=True, garbage=3)

    pdfCropMargins.crop(["dadanswers/temp/temp.pdf", "-o", "dadanswers/temp/cropped.pdf"])

    image = pdf2image.convert_from_path("dadanswers/temp/cropped.pdf")[0]
    return image