const roles = ['user', 'admin'];

export default {
    roles,
    init
};

function init(store, router) {
    // Try and retrieve the user if they've signed in previously
    store.dispatch('getCurrentUser')
        .catch(err => console.log(err));

    // Configure route guards
    router.beforeEach((to, from, next) => {
        if (!to.matched.length) {
            // If no route was matched, do nothing
            next();
            return;
        }

        // Just look at the closest match?
        const route = to.matched[0];

        // If auth is not configured, continue
        if (!route.meta.hasOwnProperty('auth')) {
            next();
            return;
        }

        const auth = route.meta.auth;
        const user = store.state.cognito.user;

        if (typeof(auth) === 'boolean') {
            if (auth && !user) {
                // Authentication required and user not logged in
                next('/signin');
                return;
            }

            else if (!auth && user) {
                // Cannot be logged in and user is logged in
                next(false);
                return;
            }
        } else if (Array.isArray(auth)) {
            if (!auth.includes(user.attributes['custom:role'])) {
                // User is the wrong role
                next(false);
                return;
            }
        } else {
            next(Error('Invalid auth guard'));
            return;
        }

        next();
    });
}

