
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    scssFolder = 'boards/static/boards/sass/*.scss',
    cssFolder = 'boards/static/boards/css',
    jsFolder = 'boards/static/boards/js';

gulp.task('sassCompile', function(done){
    gulp.src(scssFolder)
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(gulp.dest(cssFolder));
    done();
});

gulp.task('watcher', function(done){
    gulp.watch(scssFolder, gulp.series('sassCompile'));
    done();
});
