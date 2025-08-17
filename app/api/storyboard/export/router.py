from fastapi import APIRouter

export_router = APIRouter(
    prefix='/export',
    tags=['storyboard-export']
)

from .excel.router import excel_router
export_router.include_router(excel_router)

from .img.router import img_router
export_router.include_router(img_router)

from .pdf.router import pdf_router
export_router.include_router(pdf_router)

from .video.router import video_router
export_router.include_router(video_router)