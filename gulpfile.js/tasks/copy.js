var gulp = require('gulp');

// Copy vendor files from /node_modules into /vendor
// NOTE: requires `npm install` before running!
gulp.task('copy', function() {
  gulp.src([
      'node_modules/bootstrap/dist/**/*',
      '!**/npm.js',
      '!**/bootstrap-theme.*',
      '!**/*.map'
    ])
    .pipe(gulp.dest('CoverYourMeds/static/vendor/bootstrap'))

    gulp.src([
      'node_modules/startbootstrap-sb-admin/**/*'
    ])
    .pipe(gulp.dest('CoverYourMeds/static/vendor/startbootstrap-sb-admin'))

    gulp.src([
      'node_modules/datatables/media/**/*'
    ])
    .pipe(gulp.dest('CoverYourMeds/static/vendor/datatables'))

  gulp.src(['node_modules/jquery/dist/jquery.js', 'node_modules/jquery/dist/jquery.min.js'])
    .pipe(gulp.dest('CoverYourMeds/static/vendor/jquery'))
})
