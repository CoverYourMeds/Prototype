var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var rename = require("gulp-rename");

// Minify CSS
gulp.task('css:minify', ['sass:compile'], function() {
  return gulp.src([
      'CoverYourMeds/static/css/*.css',
      '!CoverYourMeds/static/css/*.min.css'
    ])
    .pipe(cleanCSS())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest('CoverYourMeds/static/css'));
});
