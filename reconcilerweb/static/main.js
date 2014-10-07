var dashsocket = SocketService('dashboard.ws');

var dom = React.DOM;




var Tab = React.createClass({
    render: function(){
        (dom.div({classname: 'item'}));
    }
});

        (dom.div({classname: 'ui tabular menu'}));

var TabCollection = React.createClass({
    render: function(){
        <div class="ui tabular menu">
            <Tab>State</Tab>
            <Tab>Health</Tab>
            <Tab>Logs</Tab>
        </div>
    }
});

var Column = React.createClass({
    render: function(){
        (dom.div({classname:'column'},
                 "I'm column " + this.props.column));
    }
});

React.renderComponent(
    TabCollection(null,
                  Tab('State'),
                  Tab('Health'),
                  Tab('Logs')),
    $('content')
);

/*
     <div class="ui tabular menu">
        <a class="active item">
          State
        </a>
        <a class="item">
          Health
        </a>
        <a class="item">
          Logs
        </a>
      </div>
*/
