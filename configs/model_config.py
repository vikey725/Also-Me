import sys
import warnings
warnings.filterwarnings("ignore")
from detectron2.config import get_cfg
from typing import ClassVar, Dict

"""
configuration file for DensePose
"""

sys.path.append("../detectron2/projects/DensePose")
from densepose import add_densepose_config
from densepose.vis.bounding_box import ScoredBoundingBoxVisualizer
from densepose.vis.densepose_results import (
    DensePoseResultsContourVisualizer,
    DensePoseResultsFineSegmentationVisualizer,
    DensePoseResultsUVisualizer,
    DensePoseResultsVVisualizer,
)


cfg = get_cfg()
add_densepose_config(cfg)

cfg.merge_from_file('../detectron2/projects/DensePose/configs/densepose_rcnn_R_50_FPN_s1x.yaml')
cfg.MODEL.DEVICE = 'cuda'
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS = 'checkpoints/model_final_289019.pkl'

VISUALIZERS: ClassVar[Dict[str, object]] = {
    'dp_contour': DensePoseResultsContourVisualizer,
    'dp_segm': DensePoseResultsFineSegmentationVisualizer,
    'dp_u': DensePoseResultsUVisualizer,
    'dp_v': DensePoseResultsVVisualizer,
    'astype': ScoredBoundingBoxVisualizer,
}
visualizers = [
    VISUALIZERS['dp_segm'](),
    VISUALIZERS['dp_contour'](),
    VISUALIZERS['dp_u'](),
    VISUALIZERS['dp_v']()
]



