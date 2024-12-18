auto_scale_lr = dict(base_batch_size=16, enable=False)
backend_args = None
data_root = './mydataset'
dataset_type = 'CocoDataset'
default_hooks = dict(
    checkpoint=dict(interval=3, type='CheckpointHook'),
    logger=dict(interval=10, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(type='DetVisualizationHook'))
default_scope = 'mmdet'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
load_from = None
log_level = 'INFO'
log_processor = dict(by_epoch=True, type='LogProcessor', window_size=50)
max_epochs = 36
metainfo = dict(
    classes=(
        'tree',
        'canopy',
    ),
    palette=[
        (
            220,
            20,
            60,
        ),
        (
            40,
            120,
            180,
        ),
    ])
model = dict(
    backbone=dict(
        depth=50,
        frozen_stages=1,
        init_cfg=dict(checkpoint='torchvision://resnet50', type='Pretrained'),
        num_stages=4,
        out_indices=(
            0,
            1,
            2,
            3,
        ),
        style='pytorch',
        type='ResNet'),
    data_preprocessor=dict(
        bgr_to_rgb=True,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_mask=True,
        pad_size_divisor=32,
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='DetDataPreprocessor'),
    mask_head=dict(
        cls_down_index=0,
        feat_channels=512,
        in_channels=256,
        loss_cls=dict(
            alpha=0.25,
            gamma=2.0,
            loss_weight=1.0,
            type='FocalLoss',
            use_sigmoid=True),
        loss_mask=dict(loss_weight=3.0, type='DiceLoss', use_sigmoid=True),
        mask_feature_head=dict(
            end_level=3,
            feat_channels=128,
            mask_stride=4,
            norm_cfg=dict(num_groups=32, requires_grad=True, type='GN'),
            out_channels=256,
            start_level=0),
        num_classes=2,
        num_grids=[
            40,
            36,
            24,
            16,
            12,
        ],
        pos_scale=0.2,
        scale_ranges=(
            (
                1,
                96,
            ),
            (
                48,
                192,
            ),
            (
                96,
                384,
            ),
            (
                192,
                768,
            ),
            (
                384,
                2048,
            ),
        ),
        stacked_convs=4,
        strides=[
            8,
            8,
            16,
            32,
            32,
        ],
        type='SOLOV2Head'),
    neck=dict(
        in_channels=[
            256,
            512,
            1024,
            2048,
        ],
        num_outs=5,
        out_channels=256,
        start_level=0,
        type='FPN'),
    test_cfg=dict(
        filter_thr=0.05,
        kernel='gaussian',
        mask_thr=0.5,
        max_per_img=100,
        nms_pre=500,
        score_thr=0.1,
        sigma=2.0),
    type='SOLOv2')
optim_wrapper = dict(
    clip_grad=dict(max_norm=35, norm_type=2),
    optimizer=dict(lr=0.0025, momentum=0.9, type='SGD', weight_decay=0.0001),
    type='OptimWrapper')
param_scheduler = [
    dict(
        begin=0,
        by_epoch=False,
        end=500,
        start_factor=0.3333333333333333,
        type='LinearLR'),
    dict(
        begin=0,
        by_epoch=True,
        end=36,
        gamma=0.1,
        milestones=[
            27,
            33,
        ],
        type='MultiStepLR'),
]
resume = False
test_cfg = dict(type='TestLoop')
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='val.json',
        backend_args=None,
        data_prefix=dict(img='val/'),
        data_root='./mydataset',
        metainfo=dict(
            classes=(
                'tree',
                'canopy',
            ),
            palette=[
                (
                    220,
                    20,
                    60,
                ),
                (
                    40,
                    120,
                    180,
                ),
            ]),
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    ann_file='./mydataset/val.json',
    backend_args=None,
    format_only=False,
    metric='segm',
    type='CocoMetric')
test_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(keep_ratio=True, scale=(
        1333,
        800,
    ), type='Resize'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(
        meta_keys=(
            'img_id',
            'img_path',
            'ori_shape',
            'img_shape',
            'scale_factor',
        ),
        type='PackDetInputs'),
]
train_cfg = dict(max_epochs=30, type='EpochBasedTrainLoop', val_interval=3)
train_dataloader = dict(
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    batch_size=1,
    dataset=dict(
        ann_file='train.json',
        backend_args=None,
        data_prefix=dict(img='train/'),
        data_root='./mydataset',
        filter_cfg=dict(filter_empty_gt=True, min_size=32),
        metainfo=dict(
            classes=(
                'tree',
                'canopy',
            ),
            palette=[
                (
                    220,
                    20,
                    60,
                ),
                (
                    40,
                    120,
                    180,
                ),
            ]),
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(
                keep_ratio=True,
                scales=[
                    (
                        1333,
                        800,
                    ),
                    (
                        1333,
                        768,
                    ),
                    (
                        1333,
                        736,
                    ),
                    (
                        1333,
                        704,
                    ),
                    (
                        1333,
                        672,
                    ),
                    (
                        1333,
                        640,
                    ),
                ],
                type='RandomChoiceResize'),
            dict(prob=0.5, type='RandomFlip'),
            dict(type='PackDetInputs'),
        ],
        type='CocoDataset'),
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(
        keep_ratio=True,
        scales=[
            (
                1333,
                800,
            ),
            (
                1333,
                768,
            ),
            (
                1333,
                736,
            ),
            (
                1333,
                704,
            ),
            (
                1333,
                672,
            ),
            (
                1333,
                640,
            ),
        ],
        type='RandomChoiceResize'),
    dict(prob=0.5, type='RandomFlip'),
    dict(type='PackDetInputs'),
]
val_cfg = dict(type='ValLoop')
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='val.json',
        backend_args=None,
        data_prefix=dict(img='val/'),
        data_root='./mydataset',
        metainfo=dict(
            classes=(
                'tree',
                'canopy',
            ),
            palette=[
                (
                    220,
                    20,
                    60,
                ),
                (
                    40,
                    120,
                    180,
                ),
            ]),
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    ann_file='./mydataset/val.json',
    backend_args=None,
    format_only=False,
    metric='segm',
    type='CocoMetric')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='DetLocalVisualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = './work-dir/solov2'
