_base_ = '../mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)))
load_from =  'https://open-mmlab.s3.ap-northeast-2.amazonaws.com/mmdetection/v2.0/dcn/mask_rcnn_r50_fpn_dconv_c3-c5_1x_coco/mask_rcnn_r50_fpn_dconv_c3-c5_1x_coco_20200203-4d9ad43b.pth'
