_base_ = '../mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(plugins=[
        dict(
            cfg=dict(type='ContextBlock', ratio=1. / 16),
            stages=(False, True, True, True),
            position='after_conv3')
    ]))
load_from = 'https://open-mmlab.s3.ap-northeast-2.amazonaws.com/mmdetection/v2.0/gcnet/mask_rcnn_r50_fpn_r16_gcb_c3-c5_1x_coco/mask_rcnn_r50_fpn_r16_gcb_c3-c5_1x_coco_20200515_211915-187da160.pth'
