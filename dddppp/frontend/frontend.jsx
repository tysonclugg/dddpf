var Presentations = new Mongo.Collection('slides.presentation');

var App = React.createClass({
    mixins: [ReactMeteorData],
    getMeteorData() {
        Meteor.subscribe('Presentations');
        window.Presentations = Presentations;
        return {
            presentations: Presentations.find({}, {sort: {title: 1}}).fetch()
        };
    },
    render() {
        return (
            <ul>
                {this.data.presentations.map(function (presentation) {
                return <li key={presentation._id}><b>{presentation.title}</b> {presentation.subtitle}</li>;
                })}
            </ul>
        );
    }
});

if (Meteor.isClient) {
    Meteor.startup(function () {
        React.render(<App />, document.getElementById('root'));
    });
}
