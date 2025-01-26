from SideBarLogo import add_logo
import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
from streamlit_flow.state import StreamlitFlowState
import plotly.figure_factory as ff
import streamlit_shadcn_ui as ui
import pandas as pd
tab1, tab2, tab3 = st.tabs(["Convolutional 3D", "Expanded 3D", "Inflated 3D"])

with tab1:
    nodes = [StreamlitFlowNode( id='1', 
                                pos=(100, 0), 
                                data={'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                node_type='input', 
                                source_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '2',
                                (230, 0), 
                                {'content': '**MaxPool 3D** <br> 1 x 2 x 2 <br> stride 1 x 2 x 2'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '3', 
                                (370, 0), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='right', 
                                target_position='left',
                                draggable=False),
            StreamlitFlowNode(  '4', 
                                (500, 0), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '5', 
                                (650, 0), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                draggable=False),
            StreamlitFlowNode(  '6', 
                                (780, 0), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                draggable=False),
            StreamlitFlowNode(  '7', 
                                (910, 0), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2'}, 
                                'default', 
                                source_position='bottom', 
                                target_position='left',  
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '8', 
                                (910, 140), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='top', 
                                draggable=False),
            StreamlitFlowNode(  '9', 
                                (770, 140), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '10', 
                                (610, 140), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '11', 
                                (500, 140), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '12', 
                                (370, 140), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '13', 
                                (210, 130), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2 <br> padding 0 x 1 x 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '14', 
                                (100, 157), 
                                {'content': '**Softmax**'}, 
                                'output', 
                                target_position='right', 
                                style={'color': 'white', 'backgroundColor': 'orange', 'border': '2px solid white'},
                                draggable=False)
            ]


    edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('2-3', '2', '3', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('3-4', '3', '4', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('4-5', '4', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('5-6', '5', '6', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('6-7', '6', '7', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('7-8', '7', '8', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('8-9', '8', '9', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('9-10', '9', '10', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('10-11', '10', '11', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('11-12', '11', '12', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('12-13', '12', '13', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('13-14', '13', '14', animated=True,style={'strokeWidth': 5,'stroke': 'white'})
            ]

    state = StreamlitFlowState(nodes, edges)

    streamlit_flow('static_flow',
                    state,
                    fit_view=True,
                    show_controls=True,
                    hide_watermark=True)
    
    with st.expander("View Code"):
        st.header("Python version")
        st.code("3.11.4")
        st.header("Dependencies")
        st.code("torch==2.5.1+cu121")
        st.header("Python code")
        st.code("""
        import torch
        import torch.nn as nn

        class C3D(nn.Module):

            def __init__(self, num_classes, pretrained=True, inchannel=3,step=16):
                super(C3D, self).__init__()

                self.conv1 = nn.Conv3d(inchannel, 64, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.pool1 = nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2))

                self.conv2 = nn.Conv3d(64, 128, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.pool2 = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))

                self.conv3a = nn.Conv3d(128, 256, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.conv3b = nn.Conv3d(256, 256, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.pool3 = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))

                self.conv4a = nn.Conv3d(256, 512, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.conv4b = nn.Conv3d(512, 512, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.pool4 = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))

                self.conv5a = nn.Conv3d(512, 512, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.conv5b = nn.Conv3d(512, 512, kernel_size=(3, 3, 3), padding=(1, 1, 1))
                self.pool5 = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=(0, 1, 1))
            
                self.relu = nn.ReLU()

                self.__init_weight()

                if pretrained:
                    self.__load_pretrained_weights()

            def forward(self, x):
                x = self.relu(self.conv1(x))
                x = self.pool1(x)

                x = self.relu(self.conv2(x))
                x = self.pool2(x)
                
                x = self.relu(self.conv3a(x))
                x = self.relu(self.conv3b(x))
                x = self.pool3(x)

                x = self.relu(self.conv4a(x))
                x = self.relu(self.conv4b(x))
                x = self.pool4(x)

                x = self.relu(self.conv5a(x))
                x = self.relu(self.conv5b(x))
                x = self.pool5(x)

                logits = x

                return logits

            def __load_pretrained_weights(self):
                corresp_name = {
                                # Conv1
                                "features.0.weight": "conv1.weight",
                                "features.0.bias": "conv1.bias",
                                # Conv2
                                "features.3.weight": "conv2.weight",
                                "features.3.bias": "conv2.bias",
                                # Conv3a
                                "features.6.weight": "conv3a.weight",
                                "features.6.bias": "conv3a.bias",
                                # Conv3b
                                "features.8.weight": "conv3b.weight",
                                "features.8.bias": "conv3b.bias",
                                # Conv4a
                                "features.11.weight": "conv4a.weight",
                                "features.11.bias": "conv4a.bias",
                                # Conv4b
                                "features.13.weight": "conv4b.weight",
                                "features.13.bias": "conv4b.bias",
                                # Conv5a
                                "features.16.weight": "conv5a.weight",
                                "features.16.bias": "conv5a.bias",
                                # Conv5b
                                "features.18.weight": "conv5b.weight",
                                "features.18.bias": "conv5b.bias",
                                # fc6
                                "classifier.0.weight": "fc6.weight",
                                "classifier.0.bias": "fc6.bias",
                                # fc7
                                "classifier.3.weight": "fc7.weight",
                                "classifier.3.bias": "fc7.bias",
                                }

                p_dict = torch.load("C:\\Users\\isalo\\Documents\\Skripsi\\Program\\Backend\\c3d-pretrained.pth")
                s_dict = self.state_dict()
                for name in p_dict:
                    if name not in corresp_name:
                        continue
                    s_dict[corresp_name[name]] = p_dict[name]
                self.load_state_dict(s_dict)

            def __init_weight(self):
                for m in self.modules():
                    if isinstance(m, nn.Conv3d):
                        # n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                        # m.weight.data.normal_(0, math.sqrt(2. / n))
                        torch.nn.init.kaiming_normal_(m.weight)
                    elif isinstance(m, nn.BatchNorm3d):
                        m.weight.data.fill_(1)
                        m.bias.data.zero_()

        def get_1x_lr_params(model):
            
            b = [model.conv1, model.conv2, model.conv3a, model.conv3b, model.conv4a, model.conv4b,
                model.conv5a, model.conv5b, model.fc6, model.fc7]
            for i in range(len(b)):
                for k in b[i].parameters():
                    if k.requires_grad:
                        yield k

        def get_10x_lr_params(model):
            
            b = [model.fc8]
            for j in range(len(b)):
                for k in b[j].parameters():
                    if k.requires_grad:
                        yield k

        if __name__ == "__main__":
            inputs = torch.rand(1, 2, 16, 112, 112)
            model = C3D(num_classes=101, pretrained=True)

            outputs = model(inputs)
            probs = nn.Softmax(dim=1)(outputs)
            preds = torch.max(probs, 1)[1]
            print(preds)
        """)

    st.header("Evaluation")
    col1, col2 = st.columns((1,3))
    with col1:
        ui.card(title="Model Accuracy", content="80.13%", description="With loss 0.52", key="card1").render()
        with ui.card(key="cards1"):
            ui.element("div", children=["Hyperparameter"], className="text-black text-sm font-medium", key="label1")
            ui.element("div", children=["Epoch: 30"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Learning rate: 1e-5"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Batch size: 4"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Optimizer: Adam"], className="text-gray-400 text-sm font-medium", key="label2")
            
    with col2:
        z = [
            [239, 5, 23, 42, 10, 4],
            [3, 744, 36, 68, 25, 17],
            [4, 9, 496, 11, 5, 9],
            [8, 17, 41, 592, 14, 12],
            [3, 8, 20, 58, 666, 167],
            [2, 10, 28, 29, 79, 580]
            ][::-1]

        x = ['slapping', 'kicking', 'punching', 'pushing', 'strangling', 'hairgrabs']
        y =  ['hairgrabs', 'strangling', 'pushing', 'punching', 'kicking', 'slapping']

        # change each element of z to type string for annotations
        z_text = [[str(y) for y in x] for x in z]

        # set up figure 
    #     fig = ff.create_annotated_heatmap(
    #     z, x=x, y=y, annotation_text=z_text, colorscale=[[0, 'black'], [1, 'white']]
    # )
        fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale=[[0, 'black'], [1, 'white']])

        # add custom xaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.15,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom yaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.35,
                                y=0.5,
                                showarrow=False,
                                text="Real value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))

        # adjust margins to make room for yaxis title
        fig.update_layout(margin=dict(t=0,b=0,pad=0),height=325,autosize=False)

        # add colorbar
        fig['data'][0]['showscale'] = True
        st.plotly_chart(fig)

    st.header("Explanation")
    st.markdown("<div style='text-align:justify';>Convolutional Neural Networks (CNN) form the basis for the development of C3D (3D Convolutional Network) models specifically designed for processing volumetric or sequential data. Single-stream 2D CNN models have shown excellent performance in handling image classification, object segmentation, and object detection problems. However, single-stream 2D CNNs are not ideal for action recognition in video data because dynamic action recognition requires analyzing spatial and temporal information simultaneously, while 2D CNNs are only capable of learning spatial or temporal information separately. With 3D convolution, each filter is able to extract features not only from the spatial dimension (image height and width) but also from the temporal dimension (frame order). This allows neural networks to understand and analyze patterns that change over time, which is crucial for tasks such as video analysis, gesture recognition, and various other applications involving sequential data. Therefore, the use of 3D convolution in the processing of video and other temporal data has become very important in order to obtain a more comprehensive and accurate representation of such data (Tran, et al., 2015).</br>",unsafe_allow_html=True)
    # st.markdown()
with tab2:
    col1, col2 = st.columns((3,1))
    with col1:
        nodes = [StreamlitFlowNode( id='1', 
                                    pos=(100, 0), 
                                    data={'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1,2,2'}, 
                                    node_type='input', 
                                    source_position='right', 
                                    draggable=False),
                StreamlitFlowNode(  '2',
                                    (230, 18), 
                                    {'content': '4 x **Block 1**'}, 
                                    'default', 
                                    source_position='right', 
                                    target_position='left', 
                                    draggable=False),
                StreamlitFlowNode(  '3', 
                                    (330, 18), 
                                    {'content': '4 x **Block 2**'}, 
                                    'default', 
                                    source_position='right', 
                                    target_position='left',
                                    draggable=False),
                StreamlitFlowNode(  '4', 
                                    (430, 18), 
                                    {'content': '4 x **Block 3**'}, 
                                    'default', 
                                    source_position='right', 
                                    target_position='left', 
                                    draggable=False),
                StreamlitFlowNode(  '5', 
                                    (530, 18), 
                                    {'content': '4 x **Block 4**'}, 
                                    'default', 
                                    source_position='right', 
                                    target_position='left', 
                                    draggable=False),
                StreamlitFlowNode(  '6', 
                                    (630,18), 
                                    {'content': '**Adaptive Avg Pooling 3D**'}, 
                                    'default', 
                                    source_position='right', 
                                    target_position='left', 
                                    draggable=False),
                StreamlitFlowNode(  '7', 
                                    (810, 18), 
                                    {'content': '**Fully Connected**'}, 
                                    'default', 
                                    source_position='right', 
                                    target_position='left',  
                                    draggable=False),
                
                ]


        edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True, label="reLU", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'orange'},style={'strokeWidth': 5,'stroke': 'white','color':'black'}),
                StreamlitFlowEdge('2-3', '2', '3', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('3-4', '3', '4', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('4-5', '4', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('5-6', '5', '6', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('6-7', '6', '7', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                ]

        state = StreamlitFlowState(nodes, edges)

        streamlit_flow('expanded3D',
                        state,
                        fit_view=True,
                        show_controls=True,
                        hide_watermark=True)
    with col2:
        df = pd.DataFrame({'stage':['BLock 1','BLock 2','BLock 3','BLock 4'],
                           'input_size':[64,256,512,1024]})
        df.index = [''] * len(df)

        st.table(df)
        st.markdown("""
        <style>
            .stTable tr {
                height: 100px; # use this to adjust the height
                justify-content:center;
            }
            table {
                margin-left: auto;
                margin-right: auto;
            }
            table tbody td {
                text-align: center !important;
            }
            table thead th {
                text-align: center !important;
            }
        </style>
""", unsafe_allow_html=True)
        hide_index_js = """
    <script>
        const tables = window.parent.document.querySelectorAll('table');
        tables.forEach(table => {
            const indexColumn = table.querySelector('thead th:first-child');
            if (indexColumn) {
                indexColumn.style.display = 'none';
            }
            const indexCells = table.querySelectorAll('tbody th');
            indexCells.forEach(cell => {
                cell.style.display = 'none';
            });
        });
    </script>
    """

    # Use components.html to inject the JavaScript
    st.components.v1.html(hide_index_js, height=0)


    
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("<div style=color: white;'><b>First layer for each block</b> </div>",unsafe_allow_html=True)
        nodes = [StreamlitFlowNode( id='1', 
                                pos=(184, 0), 
                                data={'content': '**Conv 3D**<br>1 x 1 x 1'}, 
                                node_type='input', 
                                source_position='bottom', 
                                draggable=False),
                StreamlitFlowNode( id='1.5', 
                                pos=(184, 200), 
                                data={'content': '**Conv 3D**<br>1 x 1 x 1'}, 
                                node_type='default', 
                                source_position='bottom', 
                                draggable=False),
                StreamlitFlowNode( id='1.5.2', 
                                pos=(150, 300), 
                                data={'content': '**Batch Normalization**'}, 
                                node_type='default', 
                                source_position='bottom', 
                                draggable=False),
                StreamlitFlowNode(  '2',
                                    (34, 100), 
                                    {'content': '**Conv 3D**<br>3 x 3 x 3'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '3', 
                                    (34, 200), 
                                    {'content': '**Conv 3D**<br>1 x 1 x 1'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '4', 
                                    (0, 300), 
                                    {'content': '**Batch Normalization**'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '5', 
                                    (120, 420), 
                                    {'content': '**Add**'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '6', 
                                    (120, 500), 
                                    {'content': '**reLU**'}, 
                                    'output',  
                                    target_position='top', 
                                    draggable=False,
                                    style={'backgroundColor': 'orange'}),
                
                ]


        edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('2-3', '2', '3', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('3-4', '3', '4', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('4-5', '4', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('1-1.5', '1', '1.5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('1.5-1.5.2', '1.5', '1.5.2', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('1.5.2-5', '1.5.2', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('5-6', '5', '6', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
        ]

        state = StreamlitFlowState(nodes, edges)

        streamlit_flow('bottleneck1',
                        state,
                        fit_view=True,
                        show_minimap=False,
                        show_controls=False,
                        pan_on_drag=False,
                        allow_zoom=False,hide_watermark=True)
    with col2:
        st.markdown("<div style='text-align: end; color: white;'><b>Second - last layer for each block</b> </div>",unsafe_allow_html=True)
        nodes = [StreamlitFlowNode( id='1', 
                                pos=(150, 0), 
                                data={'content': '**Conv 3D** <br> 1 x 1 x 1'}, 
                                node_type='input', 
                                source_position='bottom', 
                                draggable=False),
                StreamlitFlowNode(  '2',
                                    (34, 100), 
                                    {'content': '**Conv 3D**<br>3 x 3 x 3'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '3', 
                                    (34, 200), 
                                    {'content': '**Conv 3D**<br>1 x 1 x 1'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '4', 
                                    (0, 300), 
                                    {'content': '**Batch Normalization**'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '5', 
                                    (164, 420), 
                                    {'content': '**Add**'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '6', 
                                    (164, 500), 
                                    {'content': '**reLU**'}, 
                                    'output',  
                                    target_position='top', 
                                    draggable=False,
                                    style={'backgroundColor': 'orange'}),
                
                ]


        edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('2-3', '2', '3', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('3-4', '3', '4', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('4-5', '4', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('1-5', '1', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'},path_type='bezier'),
                StreamlitFlowEdge('5-6', '5', '6', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
        ]

        state = StreamlitFlowState(nodes, edges)

        streamlit_flow('bottleneck2',
                        state,
                        fit_view=True,
                        show_minimap=False,
                        show_controls=False,
                        pan_on_drag=False,
                        allow_zoom=False,hide_watermark=True)
    with st.expander("View Code"):
        st.header("Python version")
        st.code("3.11.4")
        st.header("Dependencies")
        st.code("torch==2.5.1+cu121")
        st.header("Python code")
        st.code("""import torch
import torch.nn as nn
import torch.nn.functional as F


class Conv3DBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, use_bn=False, use_relu=False):
        super(Conv3DBlock, self).__init__()
        self.conv = nn.Conv3d(in_channels, out_channels, kernel_size, stride, padding, bias=True)
        self.bn = nn.BatchNorm3d(out_channels) if use_bn else nn.Identity()
        self.relu = nn.ReLU(inplace=True) if use_relu else nn.Identity()

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x


class X3D_Bottleneck(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1, expansion=4, temporal_kernel_size=3):
        super(X3D_Bottleneck, self).__init__()
        mid_channels = out_channels // expansion

        self.conv1 = Conv3DBlock(in_channels, mid_channels, kernel_size=1, stride=1, padding=0)
        self.conv2 = Conv3DBlock(
            mid_channels, mid_channels,
            kernel_size=(temporal_kernel_size, 3, 3),
            stride=(stride, stride, stride),
            padding=(temporal_kernel_size // 2, 1, 1)
        )
        self.conv3 = nn.Conv3d(mid_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=False)
        self.bn3 = nn.BatchNorm3d(out_channels)

        self.relu = nn.ReLU(inplace=True)
        self.downsample = nn.Sequential(
            nn.Conv3d(in_channels, out_channels, kernel_size=1, stride=(stride, stride, stride), bias=False),
            nn.BatchNorm3d(out_channels)
        ) if stride != 1 or in_channels != out_channels else nn.Identity()

    def forward(self, x):
        residual = self.downsample(x)
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.bn3(x)
        x += residual
        return self.relu(x)


class X3D(nn.Module):
    def __init__(self, num_classes=400, layers=(3, 3, 3, 3,3), block=X3D_Bottleneck, channels=(64, 128, 256, 512, 4096), expansion=4):
        super(X3D, self).__init__()
        self.stem = Conv3DBlock(2, channels[0], kernel_size=(3, 3, 3), stride=(1, 2, 2), padding=(2, 1, 1))

        self.layers = nn.ModuleList()
        for i, num_blocks in enumerate(layers):
            stride = 1 if i == 0 else 2
            layer = self._make_layer(block, channels[i], channels[i+1] if i+1 < len(channels) else channels[i]*expansion, num_blocks, stride)
            self.layers.append(layer)

        self.pool = nn.AdaptiveAvgPool3d(1)
        self.fc = nn.Linear(channels[-1] * expansion, num_classes)

    def _make_layer(self, block, in_channels, out_channels, blocks, stride):
        layers = [block(in_channels, out_channels, stride)]
        for _ in range(1, blocks):
            layers.append(block(out_channels, out_channels))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.stem(x)
        for layer in self.layers:
            x = layer(x)
        x = self.pool(x)
        x = x.flatten(1)
        return self.fc(x)

if __name__ == "__main__":
    model = X3D(num_classes = 6, layers = (4, 4, 4,4), channels = (64, 256, 512,1024))
    inputs = torch.rand(4, 2, 30, 112, 112)
    model(inputs)
""")
    st.header("Evaluation")
    col1, col2 = st.columns((1,3))
    with col1:
        ui.card(title="Model Accuracy", content="76.12%", description="With loss 0.65", key="card2").render()
        with ui.card(key="cards2"):
            ui.element("div", children=["Hyperparameter"], className="text-black text-sm font-medium", key="label1")
            ui.element("div", children=["Epoch: 30"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Learning rate: 1e-5"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Batch size: 4"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Optimizer: Adam"], className="text-gray-400 text-sm font-medium", key="label2")
            
    with col2:
        z = [
            [223, 5, 65, 11, 10, 4],
            [0, 618, 14, 10, 2, 4],
            [3, 10, 428, 8, 6, 18],
            [27, 122, 105, 712, 56, 46],
            [2, 12, 17, 42, 600, 143],
            [4, 26, 15, 17, 125, 574]
            ][::-1]

        x = ['slapping', 'kicking', 'punching', 'pushing', 'strangling', 'hairgrabs']
        y =  ['hairgrabs', 'strangling', 'pushing', 'punching', 'kicking', 'slapping']

        # change each element of z to type string for annotations
        z_text = [[str(y) for y in x] for x in z]

        # set up figure 
    #     fig = ff.create_annotated_heatmap(
    #     z, x=x, y=y, annotation_text=z_text, colorscale=[[0, 'black'], [1, 'white']]
    # )
        fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale=[[0, 'black'], [1, 'white']])

        # add custom xaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.15,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom yaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.35,
                                y=0.5,
                                showarrow=False,
                                text="Real value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))

        # adjust margins to make room for yaxis title
        fig.update_layout(margin=dict(t=0,b=0,pad=0),height=325,autosize=False)

        # add colorbar
        fig['data'][0]['showscale'] = True
        st.plotly_chart(fig)

    st.header("Explanation")
    st.markdown("""<div style='text-align:justify';>X3D (Expanded 3D Convolutional Network) is a deep neural network architecture used for action recognition on video data. It is an extension of the earlier Convolutional Network model, which uses 3D convolutions to capture spatial and temporal information from videos. X3D has several advantages over C3D, such as improving efficiency and performance in video action recognition systems. Also, X3D does not require high computational power for processing (Santos, et al., 2022). X3D has several size variants, such as XS (extra small), S (small), M (medium), L (large), XL (extra large), and XXL (extra extra large). The X3D model uses the concept of progressive expansion which involves a gradual increase in computational complexity and model capacity by expanding one dimension or axis at a time, such as expansion of frame rate, sampling rate, footage resolution, network depth, number of layers, and number of units (Freire-Obreg´on, Lorenzo-Navarro, Santana, Hern´andez-Sosa, & Santana, 2023).</div>""", unsafe_allow_html=True)

with tab3:
    nodes = [StreamlitFlowNode( id='1', 
                                pos=(0, 0), 
                                data={'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1,2,2'}, 
                                node_type='input', 
                                source_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '2',
                                (120, -10), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2 <br> padding 0 x 1 x 1'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '3', 
                                (280, 0), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1,2,2'}, 
                                'default', 
                                source_position='right', 
                                target_position='left',
                                draggable=False),
            StreamlitFlowNode(  '4', 
                                (400, 0), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1,2,2'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                draggable=False),
            StreamlitFlowNode(  '5', 
                                (540, -10), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2 <br> padding 0 x 1 x 1'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '6', 
                                (690,18), 
                                {'content': '**Inc 1**'}, 
                                'default', 
                                source_position='right', 
                                target_position='left',
                                draggable=False),
            StreamlitFlowNode(  '7', 
                                (770, 18), 
                                {'content': '**Inc 2**'}, 
                                'default', 
                                source_position='right', 
                                target_position='left',  
                                draggable=False),
            StreamlitFlowNode(  '8', 
                                (860, -10), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2 <br> padding 0 x 1 x 1'}, 
                                'default', 
                                source_position='right', 
                                target_position='left', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '9', 
                                (920,200), 
                                {'content': '**Inc 3**'}, 
                                'default', 
                                source_position='left', 
                                target_position='right',
                                draggable=False),
            StreamlitFlowNode(  '10', 
                                (840, 200), 
                                {'content': '**Inc 4**'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '11', 
                                (680, 172), 
                                {'content': '**MaxPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2 <br> padding 0 x 1 x 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '12', 
                                (580,200), 
                                {'content': '**Inc 5**'}, 
                                'default', 
                                source_position='left', 
                                target_position='right',
                                draggable=False),
            StreamlitFlowNode(  '13', 
                                (500, 200), 
                                {'content': '**Inc 6**'}, 
                                'default', 
                                source_position='left', 
                                target_position='right',  
                                draggable=False),
            StreamlitFlowNode(  '14', 
                                (330, 172), 
                                {'content': '**AdaptiveAvgPool 3D** <br> 2 x 2 x 2 <br> stride 2 x 2 x 2 <br> padding 0 x 1 x 1'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'},
                                draggable=False),
            StreamlitFlowNode(  '15', 
                                (220, 182), 
                                {'content': '**Conv 3D** <br> 3 x 3 x 3 <br> stride 1,2,2'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '16', 
                                (80, 200), 
                                {'content': '**Fully Connected**'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            StreamlitFlowNode(  '17', 
                                (-10, 200), 
                                {'content': '**Softmax**'}, 
                                'default', 
                                source_position='left', 
                                target_position='right', 
                                draggable=False),
            ]


    edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('2-3', '2', '3', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('3-4', '3', '4', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('4-5', '4', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('5-6', '5', '6', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('6-7', '6', '7', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('7-8', '7', '8', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('8-9', '8', '9', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('9-10', '9', '10', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('10-11', '10', '11', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('11-12', '11', '12', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('12-13', '12', '13', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('13-14', '13', '14', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('14-15', '14', '15', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('15-16', '15', '16', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            StreamlitFlowEdge('16-17', '16', '17', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
            
            ]

    state = StreamlitFlowState(nodes, edges)

    streamlit_flow('inflated3D',
                    state,
                    fit_view=True,
                    show_controls=True,
                    hide_watermark=True)
    
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("<div style= color: white;'><b>Inception Layer</b> </div>",unsafe_allow_html=True)
        nodes = [StreamlitFlowNode( id='0', 
                                pos=(-12, 0), 
                                data={'content': '**Previous Layer**'}, 
                                node_type='input', 
                                target_position='bottom', 
                                draggable=False),
                StreamlitFlowNode(  '1',
                                    (0, 150), 
                                    {'content': '**Conv 3D 1**<br>1 x 1 x 1'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '2',
                                    (100, 150), 
                                    {'content': '**Conv 3D 2**<br>1 x 1 x 1'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '3', 
                                    (200, 150), 
                                    {'content': '**Conv 3D 3**<br>1 x 1 x 1'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '4', 
                                    (300, 150), 
                                    {'content': '**MaxPool 3D**<br>3 x 3 x 3'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top',
                                    draggable=False),
                StreamlitFlowNode(  '5',
                                    (100, 250), 
                                    {'content': '**Conv 3D 4**<br>3 x 3 x 3'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '6',
                                    (200, 250), 
                                    {'content': '**Conv 3D 5**<br>3 x 3 x 3'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '7',
                                    (305, 250), 
                                    {'content': '**Conv 3D 6**<br>1 x 1 x 1'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '8',
                                    (-6, 400), 
                                    {'content': '**Concatenate**'}, 
                                    'default', 
                                    source_position='bottom', 
                                    target_position='top', 
                                    draggable=False),
                StreamlitFlowNode(  '9',
                                    (-1, 500), 
                                    {'content': '**Next Layer**'}, 
                                    'output', 
                                    target_position='top', 
                                    draggable=False),
                ]


        edges = [StreamlitFlowEdge('0-1', '0', '1', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                 StreamlitFlowEdge('0-2', '0', '2', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('0-3', '0', '3', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('0-4', '0', '4', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                
                StreamlitFlowEdge('2-5', '2', '5', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('3-6', '3', '6', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('4-7', '4', '7', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                
                StreamlitFlowEdge('1-8', '1', '8', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('5-8', '5', '8', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('6-8', '6', '8', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
                StreamlitFlowEdge('7-8', '7', '8', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),

                StreamlitFlowEdge('8-9', '8', '9', animated=True,style={'strokeWidth': 5,'stroke': 'white'}),
        ]

        state = StreamlitFlowState(nodes, edges)

        streamlit_flow('inc_module',
                        state,
                        fit_view=True,
                        show_minimap=False,
                        show_controls=False,
                        pan_on_drag=False,
                        allow_zoom=False,hide_watermark=True)
    with col2:
        st.markdown("<div style='text-align: end; color: white;'><b>Input size</b> </div>",unsafe_allow_html=True)
        df = pd.DataFrame({'Inc':['1','2','3','4','5','6'],
                           'Conv 3D 1':['192','256','480','512', '512', '512'],
                           'Conv 3D 2':['192','256','480','512','512', '512'],
                           'Conv 3D 3':['192','256','480','512','512', '512'],
                           'Conv 3D 4':['96','128','96','112','128', '144'],
                           'Conv 3D 5':['16','32','16','24','24', '32'],
                           'Conv 3D 6':['192','256','512','512', '512','512']
                           },
                           )
        df.index = [''] * len(df)

        st.table(df)
        st.markdown("""
        <style>
            .stTable tr {
                height: 70px; # use this to adjust the height
                justify-content:center;
            }
            table {
                margin-left: auto;
                margin-right: auto;
            }
            table tbody td {
                text-align: center !important;
            }
            table thead th {
                text-align: center !important;
            }
        </style>
""", unsafe_allow_html=True)
        hide_index_js = """
    <script>
        const tables = window.parent.document.querySelectorAll('table');
        tables.forEach(table => {
            const indexColumn = table.querySelector('thead th:first-child');
            if (indexColumn) {
                indexColumn.style.display = 'none';
            }
            const indexCells = table.querySelectorAll('tbody th');
            indexCells.forEach(cell => {
                cell.style.display = 'none';
            });
        });
    </script>
    """

    # Use components.html to inject the JavaScript
    st.components.v1.html(hide_index_js, height=0)


    with st.expander("View Code"):
        st.header("Python version")
        st.code("3.11.4")
        st.header("Dependencies")
        st.code("torch==2.5.1+cu121")
        st.header("Python code")
        st.code("""class Inception3D(nn.Module):
    def __init__(self, num_classes=6, dropout_prob=0.5):
        super(Inception3D, self).__init__()

        self.conv1 = nn.Conv3d(2, 64, kernel_size=(7,7,7), stride=(2,2,2), padding=(1, 1, 1))
        self.maxpool1 = nn.MaxPool3d(kernel_size=(1,3,3), stride=(1, 2, 2))

        self.conv2 = nn.Conv3d(64, 192, kernel_size=(1,1,1), stride=(1, 1, 1), padding=(1, 1, 1))
        self.conv2b = nn.Conv3d(192, 192, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))
        self.maxpool2 = nn.MaxPool3d(kernel_size=(1,3,3), stride=(1,2,2))

        self.inception3a = self._make_inception_module(192, 64, 96, 128, 16, 32, 32)
        self.inception3b = self._make_inception_module(256, 128, 128, 192, 32, 96, 64)
        self.maxpool3 = nn.MaxPool3d(kernel_size=(1,3,1), stride=(1,2,1))

        self.inception3c = self._make_inception_module(480, 192, 96, 208, 16, 48, 64)
        self.inception4a = self._make_inception_module(512, 160, 112, 224, 24, 64, 64)
        self.maxpool4 = nn.MaxPool3d(kernel_size=(2,2,2), stride=(2,2,2))


        self.inception5a = self._make_inception_module(512, 128, 128, 256, 24, 64, 64)
        self.inception5b = self._make_inception_module(512, 112, 144, 288, 32, 64, 64)
        self.avgpool = nn.AdaptiveAvgPool3d((2,7,7))
        self.dropout = nn.Dropout3d(p=dropout_prob)

        self.conv6 = nn.Conv3d(528, 6, kernel_size=(1, 1, 1), stride=(1, 1, 1), padding=(1, 1, 1))
        self.fc3 = nn.Linear(1944, 6)  # Adjust dimensions based on your input size
        self.relu = nn.ReLU()

    def _make_inception_module(self, in_channels, ch1x1, ch3x3reduce, ch3x3, ch5x5reduce, ch5x5, pool_proj):
        return nn.ModuleDict({
            'branch1': nn.Conv3d(in_channels, ch1x1, kernel_size=(1, 1, 1)),
            'branch2': nn.Sequential(
                nn.Conv3d(in_channels, ch3x3reduce, kernel_size=(1, 1, 1)),
                nn.Conv3d(ch3x3reduce, ch3x3, kernel_size=(3, 3, 3), padding=(1, 1, 1))
            ),
            'branch3': nn.Sequential(
                nn.Conv3d(in_channels, ch5x5reduce, kernel_size=(1, 1, 1)),
                nn.Conv3d(ch5x5reduce, ch5x5, kernel_size=(3, 3, 3), padding=(1,1,1))
            ),
            'branch4': nn.Sequential(
                nn.MaxPool3d(kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1)),
                nn.Conv3d(in_channels, pool_proj, kernel_size=(1, 1, 1))
            )
        })

    def forward(self, x):
        x = self.conv1(x)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.conv2b(x)
        x = self.maxpool2(x)

        x = self._forward_inception(self.inception3a, x)
        x = self._forward_inception(self.inception3b, x)
        x = self.maxpool3(x)

        x = self._forward_inception(self.inception3c, x)
        x = self._forward_inception(self.inception4a, x)
        x = self.maxpool4(x)

        x = self._forward_inception(self.inception5a, x)
        x = self._forward_inception(self.inception5b, x)
        x = self.avgpool(x)
        x = self.dropout(x)

        x =self.conv6(x)

        x = x.view(x.size(0), -1)

        x = self.fc3(x)
        x = self.relu(x)
        return x

    def _forward_inception(self, inception_module, x):
        branch1 = inception_module['branch1'](x)
        branch2 = inception_module['branch2'](x)
        branch3 = inception_module['branch3'](x)
        branch4 = inception_module['branch4'](x)

        return torch.cat([branch1, branch2, branch3, branch4], 1)

if __name__ == "__main__":
    model = Inception3D(num_classes = 6)
    inputs = torch.rand(4, 2, 30, 112, 112)
    model(inputs)
""")

    st.header("Evaluation")
    
    col1, col2 = st.columns((1,3))
    with col1:
        ui.card(title="Model Accuracy", content="54.48%", description="With loss 1.13", key="card3").render()
        with ui.card(key="cards3"):
            ui.element("div", children=["Hyperparameter"], className="text-black text-sm font-medium", key="label1")
            ui.element("div", children=["Epoch: 30"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Learning rate: 1e-5"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Batch size: 4"], className="text-gray-400 text-sm font-medium", key="label2")
            ui.element("div", children=["Optimizer: Adam"], className="text-gray-400 text-sm font-medium", key="label2")
            
    with col2:
        z = [
            [57, 7, 21, 20, 8, 5],
            [13, 478, 52, 105, 21, 24],
            [120, 78, 440, 79, 25, 39],
            [45, 131, 58, 392, 64, 59],
            [17, 35, 32, 104, 492, 278],
            [7, 64, 41, 100, 189, 384]
            ][::-1]

        x = ['slapping', 'kicking', 'punching', 'pushing', 'strangling', 'hairgrabs']
        y =  ['hairgrabs', 'strangling', 'pushing', 'punching', 'kicking', 'slapping']

        # change each element of z to type string for annotations
        z_text = [[str(y) for y in x] for x in z]

        # set up figure 
    #     fig = ff.create_annotated_heatmap(
    #     z, x=x, y=y, annotation_text=z_text, colorscale=[[0, 'black'], [1, 'white']]
    # )
        fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale=[[0, 'black'], [1, 'white']])

        # add custom xaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.15,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom yaxis title
        fig.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.35,
                                y=0.5,
                                showarrow=False,
                                text="Real value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))

        # adjust margins to make room for yaxis title
        fig.update_layout(margin=dict(t=0,b=0,pad=0),height=325,autosize=False)

        # add colorbar
        fig['data'][0]['showscale'] = True
        st.plotly_chart(fig)

    

    st.header("Explanation")
    st.markdown("""<div style='text-align:justify';>I3D (Inflated 3D Convolutional Network) is an innovative architecture in the deep learning domain, specifically designed for video data processing. The main innovation of I3D is to extend the 2D convolution weights, which have undergone an inflation process, into 3D convolution weights. This approach allows the network to capture information from both the spatial and temporal dimensions of the video data. The I3D model is well applied in video classification and action recognition tasks, and its structure and workflow can be described in several main steps (Yu, 2023).</div>""")
st.markdown("""
<style>
   button[data-baseweb="tab"] {
   font-size: 24px;
   margin: 0;
   width: 100%;
   }
</style>
""",unsafe_allow_html=True)



add_logo()
