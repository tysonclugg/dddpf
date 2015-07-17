var {
    Route,
    NotFoundRoute,
    DefaultRoute,
} = ReactRouter;

var routes = (
    <Route name="root" handler={AppHome} path="/">
        <Route name="userHome" path="/:userName" handler={UserHome} />
        <Route name="presentationHome" path="/presentation/:presentationId" handler={PresentationHome} />
        <Route name="sessionHome" path="/session/:sessionId" handler={SessionHome} />
        <Route name="sessionPending" path="/session/:sessionId/pending" handler={SessionPending} />
        <Route name="sessionPaused" path="/session/:sessionId/paused" handler={SessionPaused} />
        <Route name="sessionProblem" path="/session/:sessionId/problem" handler={SessionProblem} />
        <Route name="sessionBreak" path="/session/:sessionId/break" handler={SessionBreak} />
        <Route name="sessionForum" path="/session/:sessionId/forum" handler={SessionClosed} />
        <Route name="sessionClosed" path="/session/:sessionId/closed" handler={SessionClosed} />
        <Route name="slideView" path="/session/:sessionId/:slideId" handler={SlideView} />
    </Route>
)

var router = ReactRouter.create({
    routes: routes,
    location: ReactRouter.HistoryLocation,
});

var subsReady;

var handles = [
    Meteor.subscribe("CurrentSessions"),
];

Meteor.startup(function() {
    router.run(function (Handler, state) {
        if (state.routes.length > 1 && state.routes[1].isDefault && subsReady) {
            console.log("wahoo.");
        }

        React.render(<Handler handles={ handles } />, document.body);
    });
});

Tracker.autorun(function(computation) {
    subsReady = _.all(handles, function(handle) {
        return handle.ready();
    });

    if (subsReady && router.getRouteAtDepth(1) &&
    router.getRouteAtDepth(1).isDefault) {
        console.log("Yippee!");
        computation.stop();
    }
});
